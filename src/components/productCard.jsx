import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCartShopping } from "@fortawesome/free-solid-svg-icons";

function productCard({ product }) {
  return (
    <div className="card h-100" style={{ width: "18rem" }}>
      <img
        src={
          product.images[0]
            ? product.images[0].image
            : "https://picsum.photos/200"
        }
        alt={product.slug}
        className="card-img-top"
      />
      <div className="card-body d-flex flex-column justify-content-between">
        <div className="mb-3">
          <h5 className="card-title">{product.title}</h5>
          <p className="card-text">{product.description}</p>
        </div>
        <div>
          <p className="card-text">
            <strong>${product.unit_price}</strong>
          </p>
          <button className="btn btn-primary">
            Add to cart <FontAwesomeIcon icon={faCartShopping} />
          </button>
        </div>
      </div>
    </div>
  );
}

export default productCard;
