/* For datatable view */
jQuery.fn.dataTableExt.oApi.fnSetFilteringDelay = function ( oSettings, iDelay ) {
    var _that = this;

    if ( iDelay === undefined ) {
        iDelay = 250;
    }

    this.each( function ( i ) {
        $.fn.dataTableExt.iApiIndex = i;
        var
            $this = this,
            oTimerId = null,
            sPreviousSearch = null,
            anControl = $( 'input', _that.fnSettings().aanFeatures.f );

            anControl.unbind( 'keyup' ).bind( 'keyup', function() {
            var $$this = $this;

            if (sPreviousSearch === null || sPreviousSearch != anControl.val()) {
                window.clearTimeout(oTimerId);
                sPreviousSearch = anControl.val();
                oTimerId = window.setTimeout(function() {
                    $.fn.dataTableExt.iApiIndex = i;
                    _that.fnFilter( anControl.val() );
                }, iDelay);
            }
        });

        return this;
    } );
    return this;
};
var datatableview = {
    auto_initialize: true,
    defaults: {
        "bServerSide": true,
        // Toffee: Changed the Pagination Type to Bootstrap
        'sPaginationType': 'bootstrap'
    },

    make_xeditable: function(options) {
        var options = $.extend({}, options);
        if (!options.ajaxOptions) {
            options.ajaxOptions = {}
        }
        if (!options.ajaxOptions.headers) {
            options.ajaxOptions.headers = {}
        }
        options.ajaxOptions.headers['X-CSRFToken'] = datatableview.getCookie('csrftoken');
        options.success = function (response, newValue) {
            if (response.status == 'error') {
                return response.msg;
            }
        }
        return function(nRow, mData, iDisplayIndex) {
            $('td a[data-xeditable]', nRow).editable(options);
            return nRow;
        }
    },

    getCookie: function(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },

    initialize: function($$, opts) {
        if (typeof window.console === "undefined" || typeof window.console.log === "undefined") {
            console = {
                log: function(){},
                info: function(){}
            };
        }
        var options_name_map = {
            'sortable': 'bSortable',
            'sorting': 'aaSorting',
            'visible': 'bVisible',
        };

        var template_clear_button = $('<a href="#" class="clear-search">Clear</a>');

        $$.each(function(){
            var datatable = $(this);
            var column_options = [];
            var sorting_options = [];

            datatable.find('thead th').each(function(){
                var header = $(this);
                var options = {};
                for (var i = 0; i < header[0].attributes.length; i++) {
                    var attr = header[0].attributes[i];
                    if (attr.specified && /^data-/.test(attr.name)) {
                        var name = attr.name.replace(/^data-/, '');
                        var value = attr.value;

                        // Typecasting out of string
                        name = options_name_map[name];
                        if (/^b/.test(name)) {
                            value = (value === 'true');
                        }

                        if (name == 'aaSorting') {
                            // This doesn't go in the column_options
                            var sort_info = value.split(',');
                            sort_info[1] = parseInt(sort_info[1]);
                            sorting_options.push(sort_info);
                            continue;
                        }

                        options[name] = value;
                    }
                }
                column_options.push(options);
            });

            // Arrange the sorting column requests and strip the priority information
            sorting_options.sort(function(a, b){ return a[0] - b[0] });
            for (var i = 0; i < sorting_options.length; i++) {
                sorting_options[i] = sorting_options[i].slice(1);
            }

            options = $.extend({}, datatableview.defaults, opts, {
                "aaSorting": sorting_options,
                "aoColumns": column_options,
                "sAjaxSource": datatable.attr('data-source-url'),
                "fnInfoCallback": function(oSettings, iStart, iEnd, iMax, iTotal, sPre){
                    $("#" + datatable.attr('data-result-counter-id')).html(iTotal);
                    var infoString = "Showing "+iStart +" to "+ iEnd+" of "+iTotal+" entries";
                    if (iMax != iTotal) {
                        infoString +=  " (filtered from "+iMax+" total entries)";
                    }
                    return infoString;
                }
            });
            try {
                options = confirm_datatable_options(options, datatable);
            } catch (e) {

            }

            var initialized_datatable = datatable.dataTable(options);

            try {
                initialized_datatable.fnSetFilteringDelay();
            } catch (e) {
                console.info("datatable plugin fnSetFilteringDelay not available");
            }

            var search_input = initialized_datatable.closest('.dataTables_wrapper').find('.dataTables_filter input');
            var clear_button = template_clear_button.clone().click(function(){
                $(this).trigger('clear.datatable', [initialized_datatable]);
                return false;
            }).bind('clear.datatable', function(){
                search_input.val('').keyup();
            });
            search_input.after(clear_button).after(' ');

        });

    }
}

$(function(){
    if (datatableview.auto_initialize) {
        datatableview.initialize($('.datatable'));
    }
});
