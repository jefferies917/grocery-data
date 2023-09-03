from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializer import *
import csv
import codecs
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from rest_framework.pagination import PageNumberPagination

fs = FileSystemStorage(location='tmp/')


class ReactView(generics.ListCreateAPIView):
    queryset = React.objects.all()
    serializer_class = ReactSerializer


class Pagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductViewSet(viewsets.ModelViewSet):
    # TODO this is probably named badly since it parses everything now
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        # TODO speed up this method using bulk_create, and swap out saving the file for using a serializer (already started doing this in the newer method)
        # TODO fix accent characters not outputting correctly
        
        file = request.FILES["file"]

        content = file.read()

        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors='ignore')
        reader = csv.reader(csv_file)
        next(reader)

        for id_, row in enumerate(reader):
            if not(row):
                # ignores blank rows
                continue
            (
                date,
                retailer,
                ean,
                category,
                manufacturer,
                brand,
                product_title,
                image,
                on_promotion,
                promotion_description,
                base_price,
                shelf_price,
                promoted_price,
            ) = row
            
            new_product = Product.objects.update_or_create(
                ean=ean,
                category=category,
                manufacturer=manufacturer,
                brand=brand,
                product_title=product_title,
                image=image,
            )

            new_retailer = Retailer.objects.update_or_create(
                name=retailer,
            )

            Price.objects.update_or_create(
                product=new_product[0],
                retailer=new_retailer[0],
                date=date,
                base_price=base_price,
                shelf_price=shelf_price,
                promoted_price=promoted_price,
            )

            try:
                new_product_retailer = ProductRetailer.objects.update_or_create(
                    product=new_product[0],
                    retailer=new_retailer[0],
                    on_promotion=True if on_promotion == 'TRUE' else False,
                )

                if new_product_retailer[0].on_promotion:
                    Promotion.objects.update_or_create(
                        description=promotion_description,
                        product_retailer=new_product_retailer[0],
                    )
            except IntegrityError:
                # caused by ProductRetailer not satisfying the unique_together constraint
                continue

        return Response('Successfully uploaded the data.')
    
    @action(detail=False, methods=['POST'])
    def upload_data_with_validation(self, request):
        # TODO There is already validation built into the models but we could be extra sure and display that error back to the user instead of causing a server error
        file = request.FILES.get("file")

        reader = csv.DictReader(codecs.iterdecode(file, 'utf-8-sig'), delimiter=",")

        data = list(reader)
        print(f'Data: {data}')

        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        print(f'Serialized data: {serializer.data}')  # TODO serialize correctly

        product_list = []
        for row in serializer.data:
            print(row)
            product_list.append(
                Product(
                    ean=row["ean"],
                    category=row["Category"],
                    manufacturer=row["Manufacturer"],
                    brand=row["Brand"],
                    product_title=row["Product Title"],
                    image=row["Image"],
                )
            )

        Product.objects.bulk_create(product_list)

        return Response("Successfully Uploaded the data.")