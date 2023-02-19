using Microsoft.AspNetCore.Mvc;

namespace WebApi.DTOs;

public class TypeOfSpeechFilterDto
{
    public string[] PoliticalParty { get; set; } = Array.Empty<string>();
    public string? Legislature { get; set; }
    public int? MeetingNumber { get; set; }
    public string? TopNumber { get; set; }
}