// function AdminDashboard() {
//   return <h1>Admin Dashboard</h1>;
// }

// export default AdminDashboard;
import { useState } from "react";
import api from "../api/axios";
import "./AdminDashboard.css";


function AdminDashboard() {
  // Department state
  const [deptName, setDeptName] = useState("");
  const [deptId, setDeptId] = useState("");
  const [deptLocation, setDeptLocation] = useState("");

  // Employee state
  const [employeeId, setEmployeeId] = useState("");
  const [salary, setSalary] = useState("");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [department, setDepartment] = useState("");


  /* ---------------- ADD DEPARTMENT ---------------- */
  const addDepartment = async () => {
    try {
      await api.post("departments/", {
        department_id: deptId,
        name: deptName,
        location: deptLocation,
      });
      alert("Department added");
      setDeptName("");
      setDeptLocation("");
    } catch (err) {
      alert("Failed to add department");
    }
  };

  /* ---------------- ADD EMPLOYEE ---------------- */
  const addEmployee = async () => {
    try {
      await api.post("employees/", {
        employee_id: employeeId,
        name,
        email,
        department: Number(department), 
        salary,
      });

      alert("Employee registered successfully");
      setEmployeeId("");
      setName("");
      setEmail("");
      setDepartment("");
      setSalary("");
    } catch (err) {
      alert("Failed to add employee");
    }
  };

  return (
  <div className="admin-container">
    <h1>Admin Dashboard</h1>

    {/* ----------- Department Section ----------- */}
    <div className="admin-card">
      <h2>Add Department</h2>
      <input
        placeholder="Department ID"
        value={deptId}
        onChange={(e) => setDeptId(e.target.value)}
      />

      <input
        placeholder="Department Name"
        value={deptName}
        onChange={(e) => setDeptName(e.target.value)}
      />
      <input
        placeholder="Location"
        value={deptLocation}
        onChange={(e) => setDeptLocation(e.target.value)}
      />
      <button onClick={addDepartment}>Add Department</button>
    </div>

    <div className="admin-divider" />

    {/* ----------- Employee Section ----------- */}
    <div className="admin-card">
      <h2>Register Employee</h2>

      
      <input
        placeholder="Employee ID"
        value={employeeId}
        onChange={(e) => setEmployeeId(e.target.value)}
      />
      <input placeholder="Full Name" value={name} onChange={e => setName(e.target.value)} />
      <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
      <input
        placeholder="Salary"
        value={salary}
        onChange={(e) => setSalary(e.target.value)}
      />
      <input placeholder="Department numeric ID (e.g. 1)" value={department} onChange={e => setDepartment(e.target.value)} />

      <button onClick={addEmployee}>Register Employee</button>
    </div>
  </div>
);

}

export default AdminDashboard;
