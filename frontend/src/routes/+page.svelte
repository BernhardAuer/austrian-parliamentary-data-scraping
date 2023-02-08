<script>
	import { ApiClient } from './../javascript-client-generated/src/ApiClient.js';
	import { WeatherForecastApi } from './../javascript-client-generated/src/api/WeatherForecastApi.js';
 import { PUBLIC_API_URL } from '$env/static/public';
// import {WebApi} from 'web_api';

// let apiInstance = new WebApi.WeatherForecastApi();
// apiInstance.getWeatherForecast((error, data, response) => {
//   if (error) {
//     console.error(error);
//   } else {
//     console.log('API called successfully. Returned data: ' + data);
//   }
// });


var client = new ApiClient();
client.basePath = PUBLIC_API_URL;
let apiInstance = new WeatherForecastApi(client);
let dataToShow = "da is no nix gladen";
function test(){

  apiInstance.getWeatherForecast((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    data = JSON.stringify(data)
    console.log('API called successfully. Returned data: ' + data);
    dataToShow= data;
  }
});

};

</script>

<h1>Willkommen bei parli.info, deinem Info-Portal zu aktuellen Themen aus dem österreichischen Parlament.</h1>
<p>Test wir mal einen Backendcall mit swagger-codegen:</p>

<button on:click="{test}">API call!</button>
<button on:click="{() =>dataToShow= 'leer'}">löschen!</button>
<p>{dataToShow}</p>