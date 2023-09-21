const options = ["Donald Trump", "Eva Osherovsky", "Hatul Hamud"];

export function populateDropdown(dropdown) {
    // populate the dropdown
    document.addEventListener("DOMContentLoaded", function () {
        for (let i = 0; i < options.length; i++) {
            const option = document.createElement("option");
            option.value = options[i];
            option.text = options[i];
            dropdown.appendChild(option);
        }
    });
}
