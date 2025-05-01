import React from "react";
import { getCurrentUser } from "../utilities/auth";

function DashboardPage() {
  const user = getCurrentUser();

  return (
    <div className="dashboard">
      <h1>Welcome {user?.role}</h1>
      <p>Metrics will be loaded here based on role and department.</p>
    </div>
  );
}

export default DashboardPage;
