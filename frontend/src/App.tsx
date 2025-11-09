import React, {useState} from "react";
import "./App.css";
import CarItem from "./components/CarItem.tsx";

type CarFromApi = any;

const App: React.FC = () => {

    const [budget, setBudget] = useState(14000);

    const [aiQuery, setAiQuery] = useState("");
    const [bodyStyle, setBodyStyle] = useState("");
    const [year, setYear] = useState<string | number>("");
    const [fuelType, setFuelType] = useState("");
    const [driveType, setDriveType] = useState("");
    const [mpg, setMpg] = useState<string>("");

    const [cars, setCars] = useState<CarFromApi[]>([]);

    const handleManualSearch = async () => {
        // build payload for backend
        const payload: any = {
            minMSRP: 14000, // you can later add a min slider if you want
            maxMSRP: budget,
        };

        if (bodyStyle) payload.bodyType = bodyStyle;
        if (fuelType) payload.fuel = fuelType;
        if (driveType) payload.transmission = driveType;
        if (year) payload.year = Number(year);
        if (mpg) {
            const mpgNum = Number(mpg);
            if (!Number.isNaN(mpgNum)) payload.minMPG = mpgNum;
        }

        setCars([]);

        try {
            const res = await fetch("http://127.0.0.1:8000/result/manual", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            });

            const data = await res.json();
            setCars(data || []);
        } catch (err) {
            console.error("Manual search error:", err);
            setCars([]);
        }
    };

    const handleAiSearch = async () => {
        const trimmed = aiQuery.trim();
        if (!trimmed) return;

        // clear current results while searching (optional)
        setCars([]);

        try {
            const res = await fetch("http://127.0.0.1:8000/result/ai", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query: trimmed }),
            });

            const data = await res.json();
            setCars(data || []);
        } catch (err) {
            console.error("AI search error:", err);
            setCars([]);
        }
    };

    //Trigger from AI Search bar
    const handleAiKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleAiSearch();
        }
    };

  return (
      <>
          <div className={"body-title"}>
              <h1>Find Your Dream Toyota</h1>
              <p>Search for cars based on what matters to you.</p>
          </div>

          <div className="app-container">

              <div className="search-filters">
                  <div className="ai-bar-container">
                        <textarea
                            placeholder='Ask AI (e.g., "Find me a hybrid SUV under 35k")'
                            className="ai-input"
                            rows={1}
                            maxLength={200}
                            onChange={(e) => {
                                setAiQuery(e.target.value);
                                e.target.style.height = "auto";
                                e.target.style.height = e.target.scrollHeight + "px";
                            }}
                            onKeyDown={handleAiKeyDown}
                        />
                        <button className="ai-send-btn" onClick={handleAiSearch}>
                            Ask AI
                        </button>
                  </div>
                  <p className={"or-label"}> or search manually</p>
                  <div className={"app-manual-search"}>
                        <div className={"manual-budget"}>
                            <div className="manual-budget-header">
                                <span className="manual-budget-label">Budget / Price Range</span>
                                <span className="manual-budget-value">
                                    ${budget.toLocaleString()}
                                </span>
                            </div>

                            <input
                                type="range"
                                min={14000}
                                max={85000}
                                step={1000}
                                value={budget}
                                onChange={(e) => setBudget(Number(e.target.value))}
                            />
                        </div>
                      <div className={"manual-specs"}>
                          <div className="manual-specs-row">
                              <select className="dropdown width-33" value={bodyStyle} onChange={(e) => setBodyStyle(e.target.value)}>
                                  <option value="">Body Style</option>
                                  <option>Sedan</option>
                                  <option>SUV</option>
                                  <option>Truck</option>
                                  <option>Coupe</option>
                              </select>
                              <select className="dropdown width-33" value={year} onChange={(e) => setYear(e.target.value)}>
                                  <option value="">Year</option>
                                  {Array.from({ length: 13 }, (_, i) => (
                                      <option key={i}>{2013 + i}</option>
                                  ))}
                              </select>
                              <select className="dropdown width-33" value={fuelType} onChange={(e) => setFuelType(e.target.value)}>
                                  <option value="">Fuel Type</option>
                                  <option>Gas</option>
                                  <option>Hybrid</option>
                                  <option>Electric</option>
                              </select>
                          </div>
                          <div className="manual-specs-row">
                              <select className="dropdown width-50" value={driveType} onChange={(e) => setDriveType(e.target.value)}>
                                  <option value="">Drive Type</option>
                                  <option>FWD</option>
                                  <option>AWD</option>
                                  <option>4x4</option>
                              </select>
                              <input
                                  type="number"
                                  placeholder="MPG"
                                  className="text-input width-50"
                                  min="1" max="100"
                                  value={mpg}
                                  onChange={(e) => setMpg(e.target.value)}
                              />
                          </div>

                      </div>

                  </div>

                  <div className="manual-actions">
                      <button className="manual-search-btn" onClick={handleManualSearch}>
                          Search with Filters
                      </button>
                  </div>

              </div>

              <div className={"search-results"}>
                  {cars.length === 0 ? (
                      <div className="empty-results">
                          <h3>Waiting for your first search</h3>
                          <p>Use the filters or ask AI to find your dream Toyota.</p>
                      </div>
                  ) :
                      <>
                          {cars.map((car: any, idx: number) => (
                              <CarItem
                                  key={idx}
                                  model={car["Model"]}
                                  year={car["Year"]}
                                  msrp={car["MSRP"]}
                                  cityMpg={car["city mpg"]}
                                  fuelType={car["Engine Fuel Type"]}
                                  driveType={car["Driven_Wheels"]}
                                  bodyStyle={car["Vehicle Style"]}
                              />
                          ))}
                      </>
                  }

                  {/*}
                  <CarItem
                      model="RAV4 Hybrid XLE"
                      year={2023}
                      msrp={34500}
                      cityMpg={41}
                      fuelType="Hybrid"
                      driveType="AWD"
                      bodyStyle="SUV"
                  />
                  {*/}
              </div>



          </div>

      </>

  );
};

export default App;

