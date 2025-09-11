document.addEventListener('DOMContentLoaded', function() {
    const filterOptions = document.querySelectorAll('.filter-option');
    const dishesGrid = document.querySelector('.dishes-grid');

    filterOptions.forEach(option => {
        option.addEventListener('click', function() {
            const section = this.closest('.filter-section');
            section.querySelectorAll('.filter-option').forEach(opt => opt.classList.remove('active'));
            this.classList.add('active');

            const category = document.querySelector('.filter-option[data-category].active')?.getAttribute('data-category') || 'all';
            const difficulty = document.querySelector('.filter-option[data-difficulty].active')?.getAttribute('data-difficulty') || 'all';

            const url = new URL(window.location.href);
            url.searchParams.set('category', category);
            url.searchParams.set('difficulty', difficulty);

            fetch(url.toString())
                .then(response => response.text())
                .then(html => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const newDishesGrid = doc.querySelector('.dishes-grid');
                    dishesGrid.innerHTML = newDishesGrid.innerHTML;
                });
        });
    });
});