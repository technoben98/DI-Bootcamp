import React, { useState } from "react";
import FormComponent from "./components/FormComponent.js";

function App() {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    age: "",
    gender: "",
    destination: "",
    nutsFree: false,
    lactoseFree: false,
    isVegan: false,
  });

  const handleChange = (e) => {
    const { value, name, type, checked } = e.target;

    type === "checkbox"
      ? setFormData((prevData) => ({ ...prevData, [name]: checked }))
      : setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  return <FormComponent handleChange={handleChange} {...formData} />;
}

export default App;
