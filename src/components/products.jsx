import React, { useEffect, useState } from "react";
import ProductCard from "./productCard";
import { getProducts } from "../services/productService";
import { refresh } from "../services/authService";

function Products(props) {
  const [products, setProducts] = useState({});

  useEffect(() => {
    async function getData() {
      try {
        const result = await getProducts();
        setProducts(result.data);
      } catch ({ response }) {
        if (response && response.status === 401) {
          if (await refresh()) getData();
          else window.location = "/products/";
        }
      }
    }

    getData();
  }, []);

  return (
    <div className="row">
      {products.results &&
        products.results.map((product) => (
          <div className="col" key={product.id}>
            <ProductCard product={product} />
          </div>
        ))}
    </div>
  );
}

export default Products;
