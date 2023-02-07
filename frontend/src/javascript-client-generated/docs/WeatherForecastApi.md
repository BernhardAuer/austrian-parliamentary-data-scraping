# WebApi.WeatherForecastApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWeatherForecast**](WeatherForecastApi.md#getWeatherForecast) | **GET** /WeatherForecast | 

<a name="getWeatherForecast"></a>
# **getWeatherForecast**
> [SpeechesMetaData] getWeatherForecast()



### Example
```javascript
import {WebApi} from 'web_api';

let apiInstance = new WebApi.WeatherForecastApi();
apiInstance.getWeatherForecast((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[SpeechesMetaData]**](SpeechesMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

