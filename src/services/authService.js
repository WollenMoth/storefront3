import jwtDecode from "jwt-decode";
import http from "./httpService";

const apiEndpoint = "/auth/jwt/";
const tokenRefreshKey = "refresh";
const tokenAccessKey = "access";

export async function login(user) {
  const { data: jwt } = await http.post(`${apiEndpoint}create/`, user);
  loginWithJwt(jwt);
}

export function loginWithJwt(jwt) {
  localStorage.setItem(tokenRefreshKey, jwt.refresh);
  localStorage.setItem(tokenAccessKey, jwt.access);
  setJwt();
}

export function logout() {
  localStorage.removeItem(tokenAccessKey);
  localStorage.removeItem(tokenRefreshKey);
  setJwt();
}

export async function refresh() {
  try {
    const refresh = localStorage.getItem(tokenRefreshKey);
    if (!refresh) return;
    const { data: jwt } = await http.post(`${apiEndpoint}refresh/`, {
      refresh,
    });
    localStorage.setItem(tokenAccessKey, jwt.access);
    setJwt();
    return true;
  } catch (error) {
    logout();
  }
}

export function getCurrentUser() {
  try {
    const jwt = localStorage.getItem(tokenAccessKey);
    return jwtDecode(jwt);
  } catch (ex) {
    return null;
  }
}

export function getJwt() {
  return localStorage.getItem(tokenAccessKey);
}

function setJwt() {
  const jwt = getJwt();
  http.setJwt(jwt && `JWT ${jwt}`, "Authorization");
}

const exportedObj = {
  login,
  loginWithJwt,
  logout,
  refresh,
  getCurrentUser,
  getJwt,
};

export default exportedObj;
