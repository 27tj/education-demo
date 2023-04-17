import { createBrowserRouter } from "react-router-dom";
import HomePage from "../pages/homePage";
import ErrorPage from "../pages/errorPage";
import LoginPage from "../pages/loginPage";

export const rootRouter = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
    errorElement: <ErrorPage />,
  },
  {
    path: "/login",
    element: <LoginPage />,
    errorElement: <ErrorPage />,
  },
  {
    path: "/sign-up",
    element: <LoginPage />,
    errorElement: <ErrorPage />,
  },
]);
