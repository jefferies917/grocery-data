from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import *


class TestModelStrings(TestCase):
    """ Testing the __str__() methods on our models """

    @classmethod
    def setUpTestData(self):
        self.product = Product.objects.create(
            ean=277907,
            category='Green Tea',
            manufacturer="Sainsbury's Supermarkets Ltd",
            brand="Sainsbury's",
            product_title="Sainsbury's Green Tea x20 Tea Bags 38g",
            image="https://s3.eu-central-1.amazonaws.com/bn.production.core-images/0000000277907,FALSE,,0.75,0.75,0.75"
        )
        self.retailer = Retailer.objects.create(
            name="Sainsbury's"
        )
        self.product_retailer = ProductRetailer.objects.create(
            product=self.product,
            retailer=self.retailer,
            on_promotion=False,
        )
        self.price = Price.objects.create(
            product=self.product,
            retailer=self.retailer,
            date="2022-02-01",
            base_price=0.75,
            shelf_price=0.75,
            promoted_price=0.75,
        )
        self.promotion = Promotion.objects.create(
            description='',
            product_retailer=self.product_retailer,
        )

    def test_product_model_str(self):
        self.assertEqual(str(self.product), "Sainsbury's Green Tea x20 Tea Bags 38g")

    def test_retailer_model_str(self):
        self.assertEqual(str(self.retailer), "Sainsbury's")

    def test_price_model_str(self):
        self.assertEqual(str(self.price), "Sainsbury's Green Tea x20 Tea Bags 38g, Sainsbury's - 0.75")

    def test_product_retailer_model_str(self):
        self.assertEqual(str(self.product_retailer), "Sainsbury's Green Tea x20 Tea Bags 38g, Sainsbury's")

    def test_promotion_model_str(self):
        self.assertEqual(str(self.promotion), "")


class TestDataIntegrity(TestCase):
    def setUp(self):
        pass
    
    def test_fields_not_null(self):
        """ Test that required field (EAN, Retailer Name, Product Title) cannot be NULL """
        pass

    def test_verify_unique_constraint(self):
        """ Verify unique fields (EAN) are enforced """
        pass

    def test_foregin_key(self):
        """ Check foregin key constraints (Product, Retailer) are enforced """
        pass

    def test_boolean_fields(self):
        """ Ensure boolean fields (On Promotion) only have True/False values """
        pass

    def test_image_urls(self):
        """ Check that image URLs are valid and accessible """
        pass


class TestRelationships(TestCase):
    def setUp(self):
        pass
    
    def test_products_associated_retailer(self):
        """ Verify that products are associated with the correct retailers in 'ProductRetailer' model """
        pass

    def test_product_references(self):
        """ Ensure each product has valid reference (category, manufacturer, brand) """
        pass

    def test_price_references(self):
        """ Validate each price record references an existing product and retailer """
        pass


class TestFunctionality(TestCase):
    def setUp(self):
        pass
    
    def test_file_upload(self):
        """ Ensure file upload endpoint can handle a file with a POST request """
        file = SimpleUploadedFile("file.csv", b"file_content", content_type="text/csv")
        response = self.client.post(reverse('product-upload-data'), {'file': file})
        assert response.status_code == 200

    def test_file_upload_correct(self):
        """ Validate file will only complete upload with correct data """
        pass
    
    def test_crud_operations(self):
        """ Test CRUD operations for each model to ensure we can manipulate records as expected """
        pass

    def test_promoted_price(self):
        """ Test promotional price is being applied if on_promotion is True """
        pass

    def test_querying(self):
        """ Test querying for product prices by date and retailer to ensure accurate pricing info """
        pass

    def test_promotion_applied(self):
        """ Validate promotions can be associated with products and description is stored correctly """
        pass


class TestPerformance(TestCase):
    def setUp(self):
        pass
    
    def test_query_performance(self):
        """ Measure performance of common queries and their response times """
        pass

    def test_load(self):
        """ Stress test database with large volume of data to evaluate scalibility """
        pass


# Other TestCases: (Concurrency, Error Handling, Security, Backup and Recovery, Indexing, Cross-Browser/Platform)