const icon = document.getElementById("icon-nasa");
const count = document.getElementById("count")
const cursor = document.getElementById("body")

let clicks = 0;
let counting = false;

icon.addEventListener("click", function () {

    if (counting) return

    if (clicks < 10) {
        clicks++;
        console.log(clicks)
    }

    if (clicks == 10) {

        counting = true

        count.classList.add("visible");

        const intervalo = setInterval(() => {
            count.innerHTML = clicks;
            clicks--;

            if (clicks < 0) {
                clearInterval(intervalo);
                count.classList.remove("visible");
                setInterval(() => {
                    cursor.classList.add("rocket");
                });
            }
        }, 1000);


    }
});

