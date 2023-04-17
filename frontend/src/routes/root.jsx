import { createBrowserRouter, Outlet } from "react-router-dom";
import HomePage from "../pages/homePage";
import ErrorPage from "../pages/errorPage";
import LoginPage from "../pages/loginPage";
import Navbar from "../components/navBar";

export const rootRouter = createBrowserRouter([
  {
    path: "/",
    element: <NavbarWrapper />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/", // yes, again
        element: <HomePage />,
      },
      {
        path: "/login",
        element: <LoginPage />,
      },
      {
        path: "/sign-up",
        element: <LoginPage />,
      },
    ],
  },
]);

function NavbarWrapper() {
  return (
    <div>
      <Navbar />
      <Outlet />
    </div>
  );
}
