document.addEventListener('DOMContentLoaded', function() {
// Initially highlight the top left card
highlightCard(1);
});

const tiles = document.querySelectorAll('.card');

// Add a click event listener to each tile
tiles.forEach(tile => {
    tile.addEventListener('click', function() {
        // Call the highlight function with the clicked tile
        highlightCard(this.getAttribute("id")); // 'this' refers to the clicked tile element
        addHighlightToCart();
    })
});


// Listen for arrow key presses
document.addEventListener('keydown', function(e) {
  const inventoryItems = document.querySelectorAll('.card');
  const cartItems = document.querySelectorAll('.cart-item');
  const currentlyHighlighted = document.querySelector('.highlight');

  if (currentlyHighlighted && currentlyHighlighted.classList.contains('card')) {
    const currentId = parseInt(document.querySelector('.highlight').id, 10);
    let newId;

    switch (e.key) {
      case 'ArrowUp':
        newId = currentId - 3; // Assuming 4 cards per row
        break;
      case 'ArrowDown':
        newId = currentId + 3;
        break;
      case 'ArrowLeft':
        newId = currentId - 1;
        if (currentId % 3 === 1) return; // Prevents moving left from the first card in a row
        break;
      case 'ArrowRight':
        newId = currentId + 1;
        if (currentId % 3 === 0) return; // Prevents moving right from the last card in a row
        break;
      default:
        return; // Exit if it's not an arrow key
    }

    if (document.getElementById(newId)) {
      highlightCard(newId);
    }
  }
  else {
    switch (e.key) {
      case 'ArrowUp':
        currentlyHighlighted.previousSibling.classList.add('highlight')
        currentlyHighlighted.classList.remove('highlight');
        break;
      case 'ArrowDown':
        console.log(currentlyHighlighted.nextSibling)
        currentlyHighlighted.nextSibling.classList.add('highlight')
        currentlyHighlighted.classList.remove('highlight');
        break;
      default:
        return; // Exit if it's not an arrow key
    }
  }
});


function highlightCard(id) {
  // Remove highlight from all cards
  document.querySelectorAll('.card').forEach(card => {
    card.classList.remove('highlight');
  });
  document.querySelectorAll('.cart-item').forEach(item => {
    item.classList.remove('highlight');
  });

  // Highlight the new card
  const newHighlightCard = document.getElementById(id);
  if (newHighlightCard) {
    newHighlightCard.classList.add('highlight');
  }
};


document.addEventListener('keydown', function(e) {
if (e.key === 'Tab') {
  e.preventDefault(); // Prevent the default tab behavior (focus next element)
  
  // Parse the current URL to find the current shelf ID
  const currentUrl = window.location.href;
  const shelfIdMatch = currentUrl.match(/\/ggrid\/(\d+)\//);

  if (shelfIdMatch) {
    const currentShelfId = parseInt(shelfIdMatch[1], 10);
    const nextShelfId = currentShelfId + 1;

    // Construct the URL for the next shelf
    const nextUrl = currentUrl.replace(/\/ggrid\/\d+\//, `/ggrid/${nextShelfId}/`);

    // Redirect to the next shelf URL
    window.location.href = nextUrl;
  }
}
});


document.addEventListener('keydown', function(e) {
// Check if both Tab and Shift keys are pressed
if (e.key === 'Tab' && e.shiftKey) {
  e.preventDefault(); // Prevent the default tab behavior

  // Parse the current URL to find the current shelf ID
  const currentUrl = window.location.href;
  const shelfIdMatch = currentUrl.match(/\/ggrid\/(\d+)\/$/);

  if (shelfIdMatch) {
    const currentShelfId = parseInt(shelfIdMatch[1], 10);
    // Calculate the ID for the previous shelf
    const prevShelfId = Math.max(1, currentShelfId - 1); // Ensure the ID doesn't go below 1

    // Construct the URL for the previous shelf
    const prevUrl = currentUrl.replace(/\/ggrid\/\d+\/$/, `/ggrid/${prevShelfId}/`);

    // Redirect to the previous shelf URL
    window.location.href = prevUrl;
  }
}
});

document.addEventListener('keydown', function(e) {
if (e.key === 'Enter') {
  e.preventDefault(); // Prevent the default tab behavior (focus next element)
  
  // Parse the current URL to find the current shelf ID
  const currentUrl = window.location.href;
  const shelfIdMatch = currentUrl.match(/\/ggrid\/(\d+)\//);

  let nextShelfId = document.getElementById('section-header').getAttribute('next-shelf');


  if (shelfIdMatch) {
    // Construct the URL for the next shelf
    const nextUrl = currentUrl.replace(/\/ggrid\/\d+\//, `/ggrid/${nextShelfId}/`);

    // Redirect to the next shelf URL
    window.location.href = nextUrl;
  }
}
});

document.addEventListener('keydown', function(e) {
if (e.key === 'Enter' && e.shiftKey) {
  e.preventDefault(); // Prevent the default tab behavior (focus next element)
  
  // Parse the current URL to find the current shelf ID
  const currentUrl = window.location.href;
  const shelfIdMatch = currentUrl.match(/\/ggrid\/(\d+)\//);

  let nextShelfId = document.getElementById('section-header').getAttribute('previous-shelf');


  if (shelfIdMatch) {
    // Construct the URL for the next shelf
    const nextUrl = currentUrl.replace(/\/ggrid\/\d+\//, `/ggrid/${nextShelfId}/`);

    // Redirect to the next shelf URL
    window.location.href = nextUrl;
  }
}
});

function highlightIngredient() {
  let modal = document.querySelector('.modal-content');
  let first_row = modal.querySelector('tr');
  first_row.classList.add('highlight');
}

document.addEventListener('keydown', function(e) {
  if (e.key === ' ') { // Check if spacebar is pressed
    e.preventDefault(); // Prevent the default spacebar action
    const inventoryItems = document.querySelectorAll('.card');
    const cartItems = document.querySelectorAll('.cart-item');
    const highlightedCard = document.querySelector('.highlight');
    // updateCartItem('CREATE', highlightedCard.getAttribute('category-pk'));

    let modalId = highlightedCard.getAttribute('data-target');
    let modalElement = document.querySelector(modalId);
    let modalInstance = new bootstrap.Modal(modalElement);
    modalInstance.show();

    highlightedCard.classList.remove('highlight')
    highlightIngredient()

    


    // if (highlightedCard && highlightedCard.classList.contains('card')) {
    //   if (highlightedCard) {
    //     const itemName = highlightedCard.querySelector('.card-text').textContent.trim();
    //     const itemID = highlightedCard.getAttribute('category-pk');
    //     const sidebar = document.querySelector('.grocery-cart'); 
    //     let cartItem = sidebar.querySelector(`[data-item-name="${itemName}"]`);

    //     //Adjust Cart Total
    //     let price = highlightedCard.querySelector('.price').textContent.trim();
    //     let cartTotal = document.querySelector('.cart-total');
    //     cartTotal.textContent = (parseFloat(cartTotal.textContent) + parseFloat(price)).toFixed(2);

    //     //Add New Cart Item
    //     if (!cartItem) {
    //       cartItem = document.createElement('div');
    //       cartItem.setAttribute('data-item-name', itemName);
    //       cartItem.setAttribute('category-pk', itemID);
    //       cartItem.setAttribute('price', price);
    //       cartItem.classList.add('cart-item');
    //       cartItem.classList.add('p-1');
    //       cartItem.classList.add('text-light')
    //       cartItem.classList.add('h5')
    //       cartItem.textContent = `${itemName}: 1`; 
    //       sidebar.appendChild(cartItem); 
    //     } else {
    //       let currentCount = parseInt(cartItem.textContent.split(': ')[1], 10);
    //       cartItem.textContent = `${itemName}: ${++currentCount}`;
    //     }
    //   }
    // }
    // else {
    //   let cartItem = highlightedCard
    //   let itemName = highlightedCard.getAttribute('data-item-name');
    //   let price = cartItem.getAttribute('price');
    //   let cartTotal = document.querySelector('.cart-total');
    //   cartTotal.textContent = (parseFloat(cartTotal.textContent) + parseFloat(price)).toFixed(2);
    //   let currentCount = parseInt(cartItem.textContent.split(': ')[1], 10);
    //   cartItem.textContent = `${itemName}: ${++currentCount}`;
    // }
  }
});

function addHighlightToCart() {
    const inventoryItems = document.querySelectorAll('.card');
    const cartItems = document.querySelectorAll('.cart-item');
    const highlightedCard = document.querySelector('.highlight');
    updateCartItem('CREATE', highlightedCard.getAttribute('category-pk'));
    


    if (highlightedCard && highlightedCard.classList.contains('card')) {
      if (highlightedCard) {
        const itemName = highlightedCard.querySelector('.card-text').textContent.trim();
        const itemID = highlightedCard.getAttribute('category-pk');
        const sidebar = document.querySelector('.grocery-cart'); 
        let cartItem = sidebar.querySelector(`[data-item-name="${itemName}"]`);

        //Adjust Cart Total
        let price = highlightedCard.querySelector('.price').textContent.trim();
        let cartTotal = document.querySelector('.cart-total');
        cartTotal.textContent = (parseFloat(cartTotal.textContent) + parseFloat(price)).toFixed(2);

        //Add New Cart Item
        if (!cartItem) {
          cartItem = document.createElement('div');
          cartItem.setAttribute('data-item-name', itemName);
          cartItem.setAttribute('category-pk', itemID);
          cartItem.setAttribute('price', price);
          cartItem.classList.add('cart-item');
          cartItem.classList.add('p-1');
          cartItem.classList.add('text-light')
          cartItem.classList.add('h5')
          cartItem.textContent = `${itemName}: 1`; 
          sidebar.appendChild(cartItem); 
        } else {
          let currentCount = parseInt(cartItem.textContent.split(': ')[1], 10);
          cartItem.textContent = `${itemName}: ${++currentCount}`;
        }
      }
    }
    else {
      let cartItem = highlightedCard
      let itemName = highlightedCard.getAttribute('data-item-name');
      let price = cartItem.getAttribute('price');
      let cartTotal = document.querySelector('.cart-total');
      cartTotal.textContent = (parseFloat(cartTotal.textContent) + parseFloat(price)).toFixed(2);
      let currentCount = parseInt(cartItem.textContent.split(': ')[1], 10);
      cartItem.textContent = `${itemName}: ${++currentCount}`;
    }
};


document.addEventListener('keydown', function(e) {
  if (e.key === 'Backspace') { // Check if Backspace key is pressed
    e.preventDefault(); // Prevent the default Backspace action
    const inventoryItems = document.querySelectorAll('.card');
    const cartItems = document.querySelectorAll('.cart-item');
    const highlightedCard = document.querySelector('.highlight');
    updateCartItem('DELETE', highlightedCard.getAttribute('category-pk'));

    if (highlightedCard && highlightedCard.classList.contains('card')) {
      if (highlightedCard) {
        const itemName = highlightedCard.querySelector('.card-text').textContent.trim();
        const sidebar = document.querySelector('.grocery-cart');
        let cartItem = sidebar.querySelector(`[data-item-name="${itemName}"]`);

        //Adjust Cart Total
        let price = highlightedCard.querySelector('.price').textContent.trim();
        let cartTotal = document.querySelector('.cart-total');
        cartTotal.textContent = (parseFloat(cartTotal.textContent) - parseFloat(price)).toFixed(2);
        
        if (cartItem) {
          let currentCount = parseInt(cartItem.textContent.split(': ')[1], 10);
          if (currentCount > 1) {
            cartItem.textContent = `${itemName}: ${--currentCount}`;
          } else {
            sidebar.removeChild(cartItem); // Remove the item from the cart if count goes to 0
          }
        }
      }
    }
    else {
      const sidebar = document.querySelector('.grocery-cart');
      let cartItem = highlightedCard
      let price = cartItem.getAttribute('price');
      let cartTotal = document.querySelector('.cart-total');
      cartTotal.textContent = (parseFloat(cartTotal.textContent) - parseFloat(price)).toFixed(2);
      let itemName = highlightedCard.getAttribute('data-item-name');
      let currentCount = parseInt(cartItem.textContent.split(': ')[1], 10);
      if (currentCount > 1) {
        cartItem.textContent = `${itemName}: ${--currentCount}`;
      } else {
        if (sidebar.childElementCount == 1) {
          cartItem.classList.remove('highlight');
          document.getElementById('1').classList.add('highlight')
        }
        else if (cartItem.nextSibling) {
          cartItem.nextSibling.classList.add('highlight');
        }
        else if (cartItem.previousSibling) {
          cartItem.previousSibling.classList.add('highlight');
        }
        else {
          highlightCard(1);
        }
        sidebar.removeChild(cartItem); // Remove the item from the cart if count goes to 0
      }
    }
  }
});

document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    const inventoryItems = document.querySelectorAll('.card');
    const cartItems = document.querySelectorAll('.cart-item');
    const currentlyHighlighted = document.querySelector('.highlight');

    if (currentlyHighlighted && currentlyHighlighted.classList.contains('card')) {
      // If the highlight is currently in the inventory, switch to the first cart item
      if (cartItems.length > 0) {
        currentlyHighlighted.classList.remove('highlight');
        cartItems[0].classList.add('highlight');
      }
    } else if (currentlyHighlighted && currentlyHighlighted.classList.contains('cart-item')) {
      // If the highlight is currently in the cart, switch to the first inventory item
      if (inventoryItems.length > 0) {
        currentlyHighlighted.classList.remove('highlight');
        inventoryItems[0].classList.add('highlight');
      }
    } else {
      // Default action if no item is currently highlighted
      if (inventoryItems.length > 0) {
        inventoryItems[0].classList.add('highlight');
      }
    }
  }
});

function updateCartItem(action, categoryId) {
  fetch('', { // Update with the correct URL to your "shelf" view
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-CSRFToken': getCookie('csrftoken'), // Function to get CSRF token from cookies
    },
    body: `action=${action}&category_id=${categoryId}`
  })
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener('keydown', function(e) {
    updateCartItem("KEYSTROKE", "1")
});
document.addEventListener('click', function(e) {
    updateCartItem("KEYSTROKE", "1")
});