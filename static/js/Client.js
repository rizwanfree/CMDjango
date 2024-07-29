var dTable;

$(document).ready(function () {
  dTable = $("#myTable").DataTable({
    ajax: {
      url: "http://127.0.0.1:8000/Client/api/clients/",
    },

    columns: [
      { data: "client_name" },
      { data: "contact_person" },
      { data: "phone_number" },
      { data: "mobile_number" },
      { data: "email" },
      { data: "city.city_name" },
      {
        data: "id",
        render: function (data) {
          return `
                    <div class="action-buttons">
                        <a href="" class="btn btn-sm btn-primary">Edit</a>
                        <a href="#" class="btn btn-sm btn-info">Details</a>
                    </div>

            `;
        },
      },
    ],
  });
});
