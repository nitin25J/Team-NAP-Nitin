const alertsGrid = document.getElementById("alertsGrid");

async function loadAlerts() {
    if (!alertsGrid) return;

    try {
        const response = await fetch(`${API_BASE}/alerts`);

        if (!response.ok) {
            throw new Error("Failed to fetch alerts");
        }

        const alerts = await response.json();

        alertsGrid.innerHTML = alerts.map((a) => {

            let tagClass = "ok";

            if (a.severity === "High" || a.severity === "Severe") {
                tagClass = "critical";
            } else if (a.severity === "Moderate") {
                tagClass = "moderate";
            }

            return `
                <div class="card hoverable alert-card">

                    <div class="alert-top">

                        <div>

                            <span class="tag ${tagClass}">
                                ${a.severity}
                            </span>

                            <div class="alert-title" style="margin-top:8px">
                                ${a.type}
                            </div>

                        </div>

                    </div>

                    <div class="alert-meta">

                        <span>District: <b>${a.district}</b></span>

                        <span>Status: <b>${a.status}</b></span>

                        <span>River: <b>${a.river ?? "N/A"}</b></span>

                    </div>

                    <p style="margin-top:12px">
                        ${a.message}
                    </p>

                    <button class="btn primary" style="margin-top:14px">

                        View Details

                    </button>

                </div>
            `;

        }).join("");

    } catch (err) {

        console.error(err);

        alertsGrid.innerHTML = "<p>Unable to load alerts.</p>";

    }
}

loadAlerts();
