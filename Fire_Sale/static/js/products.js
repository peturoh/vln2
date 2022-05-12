$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax( {
            url:'/products?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return ` <div class="col-md-3 mb-4">
                                <div class="card shadow-lg">
                                    <div class="card-body">
                                    <a href='/products/${d.id}'>
                                        <img class="img-fluid" src="${d.firstImage}" alt=""/>
                                        <h4>${d.name}</h4>
                                        <p>${d.description}</p>
                                    </a>
                                    </div>
                                </div>
                            </div>
                           `
                });
                $('.products').html(newHtml.join(''));
                $('#search-box').val(resp.search);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });

    $('#filter-dropdown').on('change', function(e) {
        e.preventDefault();
        let selectedValue = $('#filter-dropdown').val();
        let searchText = $('#search-box').val();

        let params = {
                        type: "GET",
                        success: function(resp) {
                                                    let newHtml = resp.data.map(d => {
                                                        return ` <div class="col-md-3 mb-4">
                                                                    <div class="card shadow-lg">
                                                                        <div class="card-body">
                                                                        <a href='/products/${d.id}'>
                                                                            <img class="img-fluid" src="${d.firstImage}" alt=""/>
                                                                            <h4>${d.name}</h4>
                                                                            <p>${d.description}</p>
                                                                        </a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                               `
                                                    });
                                                    $('.products').html(newHtml.join(''));
                                                    $('#filter-dropdown').val('');
                                                },
                        error: function(xhr, status, error) {
                                                                console.error(error);
                                                            }
                    };

                    if ((selectedValue !== '' && searchText !== '')) {
                        params.url = '/products?sort_by=' + selectedValue + '&search_filter=' + searchText
                    } else {
                        params.url = params.url = '/products?sort_by=' + selectedValue
                    }
        $.ajax(params)});
    });



/* DON'T DELETE YET JUST INCASE
$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax( {
            url:'/products?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return ` <div class="col-md-3 mb-4">
                                <div class="card shadow-lg">
                                    <div class="card-body">
                                    <a href='/products/${d.id}'>
                                        <img class="img-fluid" src="${d.firstImage}" alt=""/>
                                        <h4>${d.name}</h4>
                                        <p>${d.description}</p>
                                    </a>
                                    </div>
                                </div>
                            </div>
                           `
                });
                $('.products').html(newHtml.join(''));
                $('#search-box').val(resp.search);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });

    $('#filter-dropdown').on('change', function(e) {
        e.preventDefault();
        var selectedValue = $('#filter-dropdown').val();
        var searchText = $('#search-box').val();
        $.ajax( {
            url:'/products?sort_by=' + selectedValue,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return ` <div class="col-md-3 mb-4">
                                <div class="card shadow-lg">
                                    <div class="card-body">
                                    <a href='/products/${d.id}'>
                                        <img class="img-fluid" src="${d.firstImage}" alt=""/>
                                        <h4>${d.name}</h4>
                                        <p>${d.description}</p>
                                    </a>
                                    </div>
                                </div>
                            </div>
                           `
                });
                $('.products').html(newHtml.join(''));
                $('#filter-dropdown').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
});*/
