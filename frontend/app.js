const API_URL = "http://localhost:5000/graphql";

// Obtener usuarios
async function getUsers() {
  const query = `{
    users {
      id
      name
      email
    }
  }`;

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });
    const result = await response.json();
    document.getElementById("response").textContent = JSON.stringify(result.data, null, 2);
  } catch (error) {
    document.getElementById("response").textContent = `Error: ${error.message}`;
  }
}

// Crear un nuevo usuario
async function createUser() {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;

  const mutation = `
    mutation {
      createUser(id: ${Date.now()}, name: "${name}", email: "${email}") {
        id
        name
        email
      }
    }
  `;

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: mutation }),
    });
    const result = await response.json();
    document.getElementById("response").textContent = JSON.stringify(result.data, null, 2);
  } catch (error) {
    document.getElementById("response").textContent = `Error: ${error.message}`;
  }
}