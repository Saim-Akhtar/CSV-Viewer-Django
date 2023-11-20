$(document).ready( function () {
    $('#datatable').DataTable({
        "scrollX": true,
        "pagingType": "full_numbers",
        "lengthMenu": [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]],
        "order": [[0, 'asc']],
        "language": {
            "search": "_INPUT_",
            "searchPlaceholder": "Search..."
        },
    });
});