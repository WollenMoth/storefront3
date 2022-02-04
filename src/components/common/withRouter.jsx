import React from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";

function withRouter(Component) {
  const WithRouter = (props) => {
    const params = useParams();
    const navigate = useNavigate();
    const location = useLocation();
    return (
      <Component
        {...props}
        params={params}
        navigate={navigate}
        location={location}
      />
    );
  };
  return WithRouter;
}

export default withRouter;
