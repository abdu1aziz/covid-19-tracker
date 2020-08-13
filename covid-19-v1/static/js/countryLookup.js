$(document).ready(function() {

	$('#singleCountryLookup').on('submit', function(event) {

		$.ajax({
			data : {
				country_name : $('#countrySearch').val(),
			},
			type : 'POST',
			url : '/countryLookup'
		})
		.done(function(data) {

			if (data.covid_19) {
				$('#singleReqCountryName').text(data.covid_19[0]);
				$('#singleReqNewCases').text(data.covid_19[1]);
				$('#singleReqActive').text(data.covid_19[2]);
				$('#singleReqCritical').text(data.covid_19[3]);
				$('#singleReqRecovered').text(data.covid_19[4]);
				$('#singleReqNewDeaths').text(data.covid_19[5]);
				$('#singleReqTotalDeaths').text(data.covid_19[6]);
				$('#errorAlert').hide();
				$('#singleModal').modal("show");

			}
			else {
				$('#errorAlert').text(data.error).show();
			}

		});

		event.preventDefault();

	});

});