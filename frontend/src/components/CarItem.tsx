import "../App.css";


// @ts-ignore
function CarItem({model, year, msrp, cityMpg, fuelType, driveType, bodyStyle, onClick}){

    const loanMonths = 60;
    const interestRate = 0.05;
    const monthlyPayment = Math.round((msrp * (1 + interestRate)) / loanMonths);

    const mpgPercent = Math.max(0, Math.min(50, cityMpg));
    const barWidth = (mpgPercent / 50) * 100;

    return (
        <>
            <div className="car-info" onClick={onClick}>
                <div className="car-info-image">
                    <img src="../placeholder.png" alt={`${model} car`} className="car-image" />
                </div>

                <div className="car-info-data">
                    <h4 className="car-info-model">
                        {model}
                    </h4>
                    <h4 className="car-info-year">
                        {year}
                    </h4>
                </div>

                <p className="car-subtitle">
                    {bodyStyle} · {fuelType} · {driveType}
                </p>

                <div className="car-mpg-section">
                    <div className="car-mpg-header">
                        <span>City MPG</span>
                        <span>{cityMpg}</span>
                    </div>
                    <div className="car-mpg-bar">
                        <div
                            className="car-mpg-bar-fill"
                            style={{
                                width: `${barWidth}%`,
                                background:
                                    cityMpg > 35
                                        ? "linear-gradient(90deg, #4ade80, #22c55e)"
                                        : cityMpg > 25
                                            ? "linear-gradient(90deg, #facc15, #eab308)"
                                            : "linear-gradient(90deg, #f87171, #ef4444)",
                            }}
                        ></div>
                    </div>
                </div>

                <div className="car-cost-box">
                    <p className="car-msrp">MSRP: ${msrp.toLocaleString()}</p>
                    <p className="car-monthly">
                        {monthlyPayment > 0 ? `$${monthlyPayment}/mo` : "—"}
                        <span className="car-monthly-sub"> · 60 months est.</span>
                    </p>
                </div>
            </div>
        </>
    );

}

export default CarItem;