import React, { useState } from "react";
import Box from "@mui/material/Box";
import IconButton from "@mui/material/IconButton";
import OutlinedInput from "@mui/material/OutlinedInput";
import InputLabel from "@mui/material/InputLabel";
import InputAdornment from "@mui/material/InputAdornment";
import FormControl from "@mui/material/FormControl";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import Button from "@mui/material-next/Button";

function Login() {
  const [showPassword, setShowPassword] = useState(false);
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");

  const handleClickShowPassword = () => setShowPassword((show) => !show);

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const handleChange = (e, set) => {
    set(e.target.value);
  };

  const handleClick = (e) => {
    console.log(`Email: ${email} \nPassword: ${password}`);
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
      }}
    >
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
        }}
      >
        <FormControl sx={{ m: 1, width: "30ch" }} variant="outlined">
          <InputLabel htmlFor="email-input">Email</InputLabel>
          <OutlinedInput
            id="email-input"
            type="email"
            label="email"
            value={email}
            onChange={(e) => {
              handleChange(e, setEmail);
            }}
          />
        </FormControl>
        <FormControl sx={{ m: 1, width: "30ch" }} variant="outlined">
          <InputLabel htmlFor="outlined-adornment-password">
            Password
          </InputLabel>
          <OutlinedInput
            id="outlined-adornment-password"
            value={password}
            onChange={(e) => {
              handleChange(e, setPassword);
            }}
            type={showPassword ? "text" : "password"}
            endAdornment={
              <InputAdornment position="end">
                <IconButton
                  aria-label="toggle password visibility"
                  onClick={handleClickShowPassword}
                  onMouseDown={handleMouseDownPassword}
                  edge="end"
                >
                  {showPassword ? <VisibilityOff /> : <Visibility />}
                </IconButton>
              </InputAdornment>
            }
            label="Password"
          />
        </FormControl>
        <Box onClick={handleClick} sx={{ marginTop: "10px", borderRadius: '25px'}}>
        <Button
          variant="filledTonal"
          sx={{ height: "50px", width:'100%' }}
        >
          Login
        </Button>
        </Box>
      </Box>
    </Box>
  );
}

export default Login;
