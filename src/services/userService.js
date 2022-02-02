import http from "./httpService";

const apiEndpoint = "/auth/users/";

export function register(user) {
  return http.post(apiEndpoint, user);
}
