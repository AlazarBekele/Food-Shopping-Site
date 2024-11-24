
function Rating () {

    rate_counter = document.getElementById('Rating_star')

    if ( rate_counter.value == '5' || 5) {
        document.getElementById('disRate').textContent = '⭐⭐⭐⭐⭐'
    } else if ( rate_counter.value == '4' || 4 ) {
        document.getElementById('disRate').textContent = '⭐⭐⭐⭐'
    } else if ( rate_counter.textContent == '3' || 3 ) {
        document.getElementById('disRate').textContent = '⭐⭐⭐'
    } else if ( rate_counter.textContent == '2' || 2 ) {
        document.getElementById('disRate').textContent = '⭐⭐'
    } else if ( rate_counter.textContent == '1' || 1 ) {
        document.getElementById('disRate').textContent = '⭐'
    }
    // rate = document.getElementById('Rating_star').textContent = ''
}

Rating ();
rate_counter = document.getElementById('Rating_star')
console.log (rate_counter)



document.getElementById('disRate').textContent = '⭐'