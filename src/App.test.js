import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders page logo", () => {
  render(<App />);
  const logo = screen.getByText(/andrebuy/i);
  expect(logo).toBeInTheDocument();
});

test("renders home page", () => {
  render(<App />);
  const homePage = screen.getByText(/home page/i);
  expect(homePage).toBeInTheDocument();
});
