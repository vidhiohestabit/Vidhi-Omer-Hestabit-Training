const container = document.getElementById("productsContainer");
const searchInput = document.getElementById("searchInput");
const sortSelect = document.getElementById("sortSelect");

let products = [];

// Fetch Products
async function fetchProducts() {
  try {
    const response = await fetch("https://dummyjson.com/products");
    const data = await response.json();
    products = data.products;
    renderProducts(products);
  } catch (error) {
    console.error("Error fetching products:", error);
  }
}

// Render Products
function renderProducts(productArray) {
  container.innerHTML = "";

  productArray.forEach(product => {
    const card = document.createElement("div");
    card.classList.add("product-card");

    card.innerHTML = `
      <img src="${product.thumbnail}" alt="${product.title}">
      <h3>${product.title}</h3>
      <p>$${product.price}</p>
    `;

    container.appendChild(card);
  });
}

// Search Function
searchInput.addEventListener("input", () => {
  const value = searchInput.value.toLowerCase();

  const filtered = products.filter(product =>
    product.title.toLowerCase().includes(value)
  );

  renderProducts(filtered);
});

// Sort Function
sortSelect.addEventListener("change", () => {
  if (sortSelect.value === "high") {
    const sorted = [...products].sort((a, b) => b.price - a.price);
    renderProducts(sorted);
  } else {
    renderProducts(products);
  }
});

// Initialize
fetchProducts();
