import http from "./httpService";

const apiEndpoint = "/store/products/";

function productUrl(id) {
  return `${apiEndpoint}${id}/`;
}

export function getProducts() {
  return http.get(apiEndpoint);
}

export function getProduct(id) {
  return http.get(productUrl(id));
}
