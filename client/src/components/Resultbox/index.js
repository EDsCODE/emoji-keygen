import React from "react";

import "./resultbox.css";

export const Resultbox = ({ children, color }) => (
    <div className="resultbox-container" style={{ backgroundColor: color }}>
        {children}
    </div>
);
