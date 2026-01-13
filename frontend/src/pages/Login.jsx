import { useState } from "react";
import axios from "axios";
import "./Login.css";
import { useNavigate } from "react-router-dom";


function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate();
  const BACKEND_BASE_URL = import.meta.env.VITE_BACKEND_URL;;

  const handleLogin = async () => {
    try {
        // hitting on the first backend url for sending username and password
      const res = await axios.post(
        `${BACKEND_BASE_URL}/api-token-auth/`,
        { username, password }
      );

    //   storing it in a browsers
    const token = res.data.token;
    localStorage.setItem("token", res.data.token);
    alert("Login successful");


// hitting on the profile url for getting the is_staff values
    const profileRes = await axios.get(
    `${BACKEND_BASE_URL}/api/v1/profile/`,
    {
        headers: {
        Authorization: `Token ${token}`,
        },
    }
    );

    const { is_staff, is_superuser } = profileRes.data;

    
    if (is_staff || is_superuser) {
        navigate("/admin");
    } else {
        navigate("/employee");
    }
    }
    catch (err) {
      setError("Invalid username or password");
    }
  };

  return (
  <div className="login-container">
    <div className="login-box">
      <h2>Login</h2>

      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={handleLogin}>Login</button>

      {error && <p className="login-error">{error}</p>}
    </div>
  </div>
);

}

export default Login;
