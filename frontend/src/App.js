import axios from 'axios';
import React from 'react';
import Helmet from 'react-helmet';
import './styles/global.css';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "./components/ui/table"


class App extends React.Component {
  state = { details: [], }

  componentDidMount() {
    let data;
    axios.get('http://localhost:8000/products/')
      .then(res => {
        data = res.data;
        this.setState({
          details: data
        });
      })
      .catch(err => { })
  }

  render() {
    return (
      <div className='application'>
        <Helmet>
          <title>Product display</title>
          <link href="./styles/global.css" rel="stylesheet"/>
        </Helmet>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[100px]">EAN</TableHead>
              <TableHead>Product Title</TableHead>
              <TableHead>Brand</TableHead>
              <TableHead className="text-right">Manufacturer</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>

            {this.state.details.map((output, id) => (
              <TableRow>
                <TableCell className="font-medium">{output.ean}</TableCell>
                <TableCell>{output.product_title}</TableCell>
                <TableCell>{output.brand}</TableCell>
                <TableCell className="text-right">{output.manufacturer}</TableCell>
              </TableRow>
            ))}

          </TableBody>
        </Table>
      </div>
    )
  }
}

export default App;
