<script>
	import { WeatherForecastApi } from './../javascript-client-generated/src/api/WeatherForecastApi.js';
// import {WebApi} from 'web_api';

// let apiInstance = new WebApi.WeatherForecastApi();
// apiInstance.getWeatherForecast((error, data, response) => {
//   if (error) {
//     console.error(error);
//   } else {
//     console.log('API called successfully. Returned data: ' + data);
//   }
// });


let apiInstance = new WeatherForecastApi();
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