$(document).ready(() => {
    $(document).on("change", ".ssa-dropdown", (e) => {
        let pk = $(e.target).find(":selected").val()
        $.ajax({
            url: "get-csc/" + pk,
            method: "GET",
            success: (response) => {
                $(document).find(".csc-dropdown").text("")
                $(document).find(".csc-dropdown").append(`<option selected="" disabled="">--Selected--</option>`)
                $.each(response, (k, v) => {
                    $(document).find(".csc-dropdown").append(
                        `<option value="${k}">${v}</option>`
                    )
                })
            },
            error: (error) => {
                console.log(error);
            }
        })
    })

    $(document).on("change", ".csc-dropdown", (e) => {
        let pk = $(e.target).find(":selected").val()
        $.ajax({
            url: "get-station-id/" + pk,
            method: "GET",
            success: (response) => {
                $(document).find(".station_id-dropdown").text("")
                $(document).find(".station_id-dropdown").append(`<option selected="" disabled="">--Selected--</option>`)
                $.each(response, (k, v) => {
                    $(document).find(".station_id-dropdown").append(
                        `<option value="${v}">${v}</option>`
                    )
                })
            },
            error: (error) => {
                console.log(error);
            }
        })
    })
});