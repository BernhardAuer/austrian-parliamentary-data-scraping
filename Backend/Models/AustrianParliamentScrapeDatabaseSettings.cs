namespace WebApi.Models;

public class AustrianParliamentScrapeDatabaseSettings
{
    public string ConnectionString { get; set; } = null!;

    public string DatabaseName { get; set; } = null!;

    public string SpeechesMetaDataCollectionName { get; set; } = null!;
}