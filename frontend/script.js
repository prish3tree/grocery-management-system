const productForm = document.getElementById("productForm");
const productList = document.getElementById("productList");


async function loadProducts() {
    if (!productList) {
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/api/products");
        const products = await response.json();

        productList.innerHTML = "";

        products.forEach(product => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${product.product_id}</td>
                <td>${product.name}</td>
                <td>${product.category}</td>
                <td>₹${product.price}</td>
                <td>${product.stock}</td>
            `;

            productList.appendChild(row);
        });

    } catch (error) {
        console.error("Unable to load products:", error);
    }
}


if (productForm) {
    productForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const product = {
            name: document.getElementById("name").value,
            category: document.getElementById("category").value,
            price: parseFloat(document.getElementById("price").value),
            stock: parseInt(document.getElementById("stock").value)
        };

        try {
            const response = await fetch("http://localhost:5000/api/products", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(product)
            });

            const result = await response.json();

            if (response.ok) {
                alert(result.message);
                productForm.reset();
                loadProducts();
            } else {
                alert("Failed to add product.");
            }

        } catch (error) {
            console.error("Unable to add product:", error);
            alert("Could not connect to the backend.");
        }
    });
}


loadProducts();
