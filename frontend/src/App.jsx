import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [form, setForm] = useState({
    median_income: 5,
    house_age: 20,
    average_rooms: 2,
    average_bedrooms: 3,
    population: 2000,
    average_occupancy: 1,
    latitude: 6.9271,
    longitude: 79.8612,
  });

  const [price, setPrice] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setForm({
      ...form,
      [name]:
        name === "latitude" || name === "longitude"
          ? Number(value)
          : Number(value),
    });
  };

  const predict = async (e) => {
    e.preventDefault();

    const res = await axios.post("http://127.0.0.1:8000/predict", form);

    setPrice(res.data.predicted_price);
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h3>House Price Predictor</h3>
        <p className="subtitle">Enter the following details:</p>
      </header>

      <main>
        <form className="predict-form" onSubmit={predict}>
          <div className="form-row">
            <label htmlFor="median_income">Median Income</label>
            <input id="median_income" name="median_income" type="number" step="0.1" value={form.median_income} onChange={handleChange} />
          </div>

          <div className="form-row">
            <label htmlFor="house_age">House Age</label>
            <input id="house_age" name="house_age" type="number" value={form.house_age} onChange={handleChange} />
          </div>

          <div className="form-row">
            <label htmlFor="average_rooms">Average Rooms</label>
            <input id="average_rooms" name="average_rooms" type="number" step="0.1" value={form.average_rooms} onChange={handleChange} />
          </div>

          <div className="form-row">
            <label htmlFor="average_bedrooms">Average Bedrooms</label>
            <input id="average_bedrooms" name="average_bedrooms" type="number" step="0.1" value={form.average_bedrooms} onChange={handleChange} />
          </div>

          <div className="form-row">
            <label htmlFor="population">Population</label>
            <input id="population" name="population" type="number" value={form.population} onChange={handleChange} />
          </div>

          <div className="form-row">
            <label htmlFor="average_occupancy">Average Occupancy</label>
            <input id="average_occupancy" name="average_occupancy" type="number" step="0.1" value={form.average_occupancy} onChange={handleChange} />
          </div>

          <div className="form-row">
            <label htmlFor="latitude">Latitude</label>
            <input id="latitude" name="latitude" type="number" step="0.0001" value={form.latitude} onChange={handleChange} />
          </div>

          <div className="form-row">
            <label htmlFor="longitude">Longitude</label>
            <input id="longitude" name="longitude" type="number" step="0.0001" value={form.longitude} onChange={handleChange} />
          </div>

          <div className="form-actions">
            <button className="primary-btn" type="submit">Predict Price</button>
          </div>
        </form>

        {price && (
          <div className="result">Predicted Price: <strong>LKR {price.toLocaleString()}</strong></div>
        )}
      </main>
    </div>
  );
}

export default App;
