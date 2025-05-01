import React from "react";
import { Navigate } from "react-router-dom";
import { getCurrentUser } from "../utilities/auth";

const ProtectedRoute = ({ children }) => {
  const user = getCurrentUser();

  if (!user) return <Navigate to="/" replace />;

  return children;
};

export default ProtectedRoute;
