import marshal,zlib,base64
exec(base64.b64decode("aW1wb3J0IHJlcXVlc3RzLGpzb24sdGltZSxzeXMscmFuZG9tLG9zLGFyZ3BhcnNlDQppbXBvcnQgY29sb3JhbWENCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUsIEJhY2ssIFN0eWxlDQpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludA0KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUNCmNvbG9yYW1hLmluaXQoYXV0b3Jlc2V0PVRydWUpDQoNCg0KDQpwYXJzZXIgPSBhcmdwYXJzZS5Bcmd1bWVudFBhcnNlcihkZXNjcmlwdGlvbj0nOTk5IERpY2UgQm90IHwgVGhpcyBJcyBHYW1ibGluZyBCb3QgUGxhc2UgVGFrZSBPd24gWW91ciBSaXNrJykNCnBhcnNlci5hZGRfYXJndW1lbnQoDQogICAgJy1jJywnLS1iZXRzZXQnLA0KICAgIGRlZmF1bHQ9MCwNCiAgICBoZWxwPSdFbnRlciBZb3VyIEJldHNldCBOdW1iZXIgKGRlZmF1bHQ6IDApJw0KKQ0KbXlfbmFtZXNwYWNlID0gcGFyc2VyLnBhcnNlX2FyZ3MoKQ0KDQoNCg0KDQoNCndpdGggb3BlbignY29uZmlnLmpzb24nLCAncicpIGFzIG15ZmlsZToNCiAgICAgIGRhdGE9bXlmaWxlLnJlYWQoKQ0KIyBwYXJzZSBmaWxlDQpvYmogPSBqc29uLmxvYWRzKGRhdGEpDQoNCg0KcHJpbnQgKFN0eWxlLk5PUk1BTCtGb3JlLkdSRUVOKyJcbj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuIitTdHlsZS5CUklHSFQrRm9yZS5HUkVFTisiQXV0aG9yIEJ5ICAiK1N0eWxlLkRJTStGb3JlLldISVRFKyI6ICIrU3R5bGUuUkVTRVRfQUxMKyJLZWx2aW5cbiIrU3R5bGUuQlJJR0hUK0ZvcmUuR1JFRU4rIkNoYW5uZWwgWXQgIitTdHlsZS5OT1JNQUwrRm9yZS5XSElURSsiOiIrU3R5bGUuUkVTRVRfQUxMKyIgQ2FyaSBNb25leSIrU3R5bGUuQlJJR0hUK0ZvcmUuR1JFRU4rIlxuRGljZSBCb3QiK1N0eWxlLk5PUk1BTCtGb3JlLldISVRFKyIgfCAiK1N0eWxlLkJSSUdIVCtGb3JlLlJFRCsiTG9zZSBTdHJlYWsgIitTdHlsZS5OT1JNQUwrRm9yZS5XSElURSsifCIrU3R5bGUuQlJJR0hUK0ZvcmUuR1JFRU4rIiBXaW4gU3RyZWFrXG4iK1N0eWxlLkJSSUdIVCtGb3JlLkdSRUVOKyJTdXBwb3J0IGJ5IGh0dHBzOi8vZ2l0aHViLmNvbS9rbHZpbm5uL2pla1xuIitTdHlsZS5CUklHSFQrRm9yZS5HUkVFTisiRG9uYXRlICIrU3R5bGUuTk9STUFMK0ZvcmUuV0hJVEUrIjoiK1N0eWxlLkJSSUdIVCtGb3JlLkdSRUVOKyIgQlRDICIrU3R5bGUuUkVTRVRfQUxMKyIxN0g0dEF6Y2ZpUDhKRW1ZUTJCUTRnUWZWZlRtTmpwY2I4XG4iK1N0eWxlLkJSSUdIVCtGb3JlLkdSRUVOKyIgICAgICAgICBMVEMgIitTdHlsZS5SRVNFVF9BTEwrIkxSWXRYZ0dWRDM4dEZISzhWUlExOFJNSlR2VWtTS1ZoZ3dcbiIrU3R5bGUuQlJJR0hUK0ZvcmUuR1JFRU4rIiAgICAgICAgIERvZ2UgIitTdHlsZS5SRVNFVF9BTEwrIkRSeFpqRDNQcmZmb1JpMUZmc2p4cWFoenJndXppVGVDNlRcblxuIikNCg0KaGlqYXUgPSBTdHlsZS5CUklHSFQrRm9yZS5HUkVFTg0KDQpyZXMgPSBTdHlsZS5SRVNFVF9BTEwNCmFidTIgPSBTdHlsZS5OT1JNQUwrRm9yZS5XSElURQ0KdW5ndSA9IFN0eWxlLk5PUk1BTCtGb3JlLk1BR0VOVEENCmhpamF1MiA9IFN0eWxlLk5PUk1BTCtGb3JlLkdSRUVODQpyZWQyID0gU3R5bGUuTk9STUFMK0ZvcmUuUkVEDQpyZWQgPSBTdHlsZS5CUklHSFQrRm9yZS5SRUQNCmMgPSByZXF1ZXN0cy5zZXNzaW9uKCkNCg0KdXJsID0gImh0dHBzOi8vd3d3Ljk5OWRvZ2UuY29tL2FwaS93ZWIuYXNweCINCnVhID0gew0KICJPcmlnaW4iOiAiZmlsZTovLyIsDQogInVzZXItYWdlbnQiOiBvYmpbIlVzZXItQWdlbnQiXSwNCiAiQ29udGVudC10eXBlIjogImFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZCIsDQogIkFjY2VwdCI6ICIqLyoiLA0KICJBY2NlcHQtTGFuZ3VhZ2UiOiAiaWQtSUQsaWQ7cT0wLjksZW4tVVM7cT0wLjgsZW47cT0wLjciLA0KICJYLVJlcXVlc3RlZC1XaXRoIjogImNvbS5yZWxhbmQucmVsYW5kaWNlYm90Ig0KfQ0KDQpkZWYga29udmVydChwZXJzZW4sdGFydWhhbik6DQogICAgZ2xvYmFsIGhpZ2gNCiAgICBnbG9iYWwgbG93DQogICAgYyA9IHN0cig5OTk5OTkgKiBmbG9hdChwZXJzZW4pIC8gMTAwKQ0KICAgIGlmIHRhcnVoYW4gPT0gIkhpIiBvciB0YXJ1aGFuID09ICJoaSIgb3IgdGFydWhhbiA9PSAiSEkiOg0KICAgICAgIG4gPSBzdHIoYy5zcGxpdCgiLiIpWzFdKQ0KICAgICAgIHBhbmdrYXQgPSA2IC0gbGVuKG4pDQogICAgICAgbG93ID0gaW50KGludChuKSAqICgxMCAqKiBwYW5na2F0KSkNCiAgICAgICBoaWdoID0gOTk5OTk5DQogICAgaWYgdGFydWhhbiA9PSAiTG8iIG9yIHRhcnVoYW4gPT0gIkxPVyIgb3IgdGFydWhhbiA9PSAibG93IiBvciB0YXJ1aGFuID09ICJMb3ciIG9yIHRhcnVoYW4gPT0gIkxPIjoNCiAgICAgICBsb3cgPSAwDQogICAgICAgaGlnaCA9IGludChjLnNwbGl0KCIuIilbMF0pDQoNCg0KZGVmIHJldihudW0pOg0KICAgIGlmIChsZW4obnVtKSA8IDgpOg0KICAgICAgICBwYW5qYW5nX25vbCA9IGludCg4IC0gbGVuKG51bSkpDQogICAgICAgIG51bSA9ICgocGFuamFuZ19ub2wqIjAiKStzdHIobnVtKSkNCiAgICAgICAgcmVzdWx0ID0gKCIwLiIrbnVtKQ0KICAgIGlmIChsZW4obnVtKSA9PSA4KToNCiAgICAgICAgcGFuamFuZ19ub2wgPSBpbnQoOCAtIGxlbihudW0pKQ0KICAgICAgICBudW0gPSAoKHBhbmphbmdfbm9sKiIwIikrc3RyKG51bSkpDQogICAgICAgIHJlc3VsdCA9ICgiMC4iK251bSkNCiAgICBlbHNlOg0KICAgICAgICBsZW5fbnVtID0gbGVuKG51bSkNCiAgICAgICAgZW5kID0gbnVtWy04Ol0NCiAgICAgICAgZmlyc3QgPSBudW1bOmxlbl9udW0tOF0NCiAgICAgICAgcmVzdWx0ID0gKGZpcnN0KyIuIitlbmQpDQogICAgcmV0dXJuIChyZXN1bHQpDQoNCg0KDQpkZWYgZGljZSh3cyxscyk6DQogICBpZiBteV9uYW1lc3BhY2UuYmV0c2V0ID09ICJBdXRvIiBvciBteV9uYW1lc3BhY2UuYmV0c2V0ID09ICJhdXRvIiBvciBteV9uYW1lc3BhY2UuYmV0c2V0ID09ICJBVVRPIjoNCiAgICAgIHVydXQgPSAwDQogICAgICBqdW1sYWh1bGFuZz0gMA0KICAgICAgd2hpbGUgVHJ1ZToNCiAgICAgICAgIGp1bWxhaHVsYW5nKz0xDQogICAgICAgICB0cnk6DQogICAgICAgICAgICAgcGVzYW4gPSBvYmpbIkNvbmZpZyJdW2p1bWxhaHVsYW5nXVsiTmFtZSBCZXQgU2V0Il0NCiAgICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgICBicmVhaw0KICAgZWxzZToNCiAgICAgIHVydXQgPSBpbnQobXlfbmFtZXNwYWNlLmJldHNldCkNCg0KICAgc2xwID0gaW50KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkludGVydmFsIl0pIC8gMTAwMA0KICAgbGltaXRfYSA9IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJSZXNldCBJZiBXaW4iXSkgLSAxDQogICBwYXlpbiA9IGludChmbG9hdChvYmpbIkNvbmZpZyJdW3VydXRdWyJCYXNlIEJldCJdKSooMTAgKiogOCkpDQogICBrb252ZXJ0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkNoYW5jZSJdLG9ialsiQ29uZmlnIl1bdXJ1dF1bIkJldCJdWyJCZXQiXSkNCiAgIGFtb3VudCA9IHBheWluDQogICBkYXRhID0gew0KICAgICAgImEiOiAiUGxhY2VCZXQiLA0KICAgICAgInMiOiBqc1siU2Vzc2lvbkNvb2tpZSJdLA0KICAgICAgIlBheUluIjogYW1vdW50LA0KICAgICAgIkxvdyI6IGxvdywNCiAgICAgICJIaWdoIjogaGlnaCwNCiAgICAgICJDbGllbnRTZWVkIjogcmFuZGludCgwLDk5OTk5OSksDQogICAgICAiQ3VycmVuY3kiOiAiZG9nZSIsDQogICAgICAiUHJvdG9jb2xWZXJzaW9uIjogIjIiDQogICB9DQogICB0cnk6DQogICAgIHIxID0gYy5wb3N0KHVybCxoZWFkZXJzPXVhLGRhdGE9ZGF0YSkNCiAgICAganNuID0ganNvbi5sb2FkcyhyMS50ZXh0KQ0KICAgICBqdW1ibCA9IGpzblsiU3RhcnRpbmdCYWxhbmNlIl0gKyBpbnQoanNuWyJQYXlPdXQiXSkgLSBpbnQoYW1vdW50KQ0KICAgICBqdW0gPSBpbnQoanNuWyJQYXlPdXQiXSkgLSBpbnQoYW1vdW50KQ0KICAgICBwcm9mID0gKGZsb2F0KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0gKyBpbnQoanNuWyJQYXlPdXQiXSkgLSBpbnQoYW1vdW50KSAtIGp1bWJsKS8oMTAgKiogOCkpDQogICAgIHByaW50IChoaWphdSsiXG5cblxuU3RhcnRpbmcgQmFsYW5jZSIscmVzK3N0cigoZmxvYXQoaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkpLygxMCAqKiA4KSkpKQ0KICAgICBwcmludCAoIkFuZGEgTWVuZ2d1bmFrYW4gQmV0U2V0IEtlICIrb2JqWyJDb25maWciXVt1cnV0XVsiTmFtZSBCZXQgU2V0Il0pDQogICAgIG4gPSAwDQogICAgIGJ1cnN0ID0gRmFsc2UNCiAgICAgc3RhdHNfcm9sZWJldF9sb3NlID0gRmFsc2UNCiAgICAgc3RhdHNfcm9sZWJldF93aW4gPSBGYWxzZQ0KICAgICBtZW5pdCA9IGRhdGV0aW1lLm5vdygpLnN0cmZ0aW1lKCclTScpDQogICAgIG1lbml0ID0gaW50KG1lbml0KSArIGludChvYmpbIkludGVydmFsIl0pDQogICAgIG5vX3dpbiA9IDANCiAgICAgbm9fbG9zZSA9IDANCiAgICAgdG90YWxfd2luPTANCiAgICAgdG90YWxfbG9zZT0wDQogICAgIG5vX3JvbGViZXQgPSAwDQogICAgIHJvbGViZXQ9IkhpIg0KICAgICByZXNldF9pZl9wcm9maXQgPSBvYmpbIkNvbmZpZyJdW3VydXRdWyJSZXNldCBJZiBQcm9maXQiXQ0KICAgICB0b3RfaWZfcHJvZml0ID0gb2JqWyJDb25maWciXVt1cnV0XVsiUmVzZXQgSWYgUHJvZml0Il0NCiAgICAgd2hpbGUgVHJ1ZToNCiAgICAgICAgaWYgcmVzZXRfaWZfcHJvZml0ID09ICJPRkYiIG9yIHJlc2V0X2lmX3Byb2ZpdCA9PSAiT2ZmIiBvciByZXNldF9pZl9wcm9maXQgPT0gIm9mZiI6DQogICAgICAgICAgIHN0YXRzX2lmX3Byb2ZpdCA9IEZhbHNlDQogICAgICAgIGVsc2U6DQogICAgICAgICAgIHN0YXRzX2lmX3Byb2ZpdCA9IFRydWUNCiAgICAgICAgaWYgb2JqWyJDb25maWciXVt1cnV0XVsiTWF4IEJldCJdID09ICJPRkYiIG9yIG9ialsiQ29uZmlnIl1bdXJ1dF1bIk1heCBCZXQiXSA9PSAib2ZmIiBvciBvYmpbIkNvbmZpZyJdW3VydXRdWyJNYXggQmV0Il0gPT0gIk9mZiI6DQogICAgICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKCIiKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICBpZiBhbW91bnQgPiBpbnQoZmxvYXQob2JqWyJDb25maWciXVt1cnV0XVsiTWF4IEJldCJdKSooMTAgKiogOCkpOg0KICAgICAgICAgICAgICAgYW1vdW50ID0gcGF5aW4NCiAgICAgICAgaWYgb2JqWyJDb25maWciXVt1cnV0XVsiQmV0Il1bIkhpIC8gTG93Il1bIlRvZ2dsZSJdID09ICJPbiIgb3Igb2JqWyJDb25maWciXVt1cnV0XVsiQmV0Il1bIkhpIC8gTG93Il1bIlRvZ2dsZSJdID09ICJPTiIgb3Igb2JqWyJDb25maWciXVt1cnV0XVsiQmV0Il1bIkhpIC8gTG93Il1bIlRvZ2dsZSJdID09ICJvbiI6DQogICAgICAgICAgICBub19yb2xlYmV0ICs9MQ0KICAgICAgICAgICAgaWYgc3RhdHNfcm9sZWJldF93aW4gaXMgVHJ1ZToNCiAgICAgICAgICAgICAgIGlmIG5vX3JvbGViZXQgPiBpbnQob2JqWyJDb25maWciXVt1cnV0XVsiQmV0Il1bIkhpIC8gTG93Il1bIklmIFdpbiJdKSAtIDE6DQogICAgICAgICAgICAgICAgICByb2xlYmV0ID0gIkxvIg0KICAgICAgICAgICAgICAgaWYgbm9fcm9sZWJldCA+IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiSGkgLyBMb3ciXVsiSWYgV2luIl0pICogMiAtIDE6DQogICAgICAgICAgICAgICAgICByb2xlYmV0ID0gIkhpIg0KICAgICAgICAgICAgICAgICAgbm9fcm9sZWJldCA9IDANCiAgICAgICAgICAgIGlmIHN0YXRzX3JvbGViZXRfbG9zZSBpcyBUcnVlOg0KICAgICAgICAgICAgICAgaWYgbm9fcm9sZWJldCA+IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiSGkgLyBMb3ciXVsiSWYgTG9zZSJdKSAtMSA6DQogICAgICAgICAgICAgICAgICByb2xlYmV0ID0gIkxvIg0KICAgICAgICAgICAgICAgaWYgbm9fcm9sZWJldCA+IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJCZXQiXVsiSGkgLyBMb3ciXVsiSWYgTG9zZSJdKSAqIDIgLSAxOg0KICAgICAgICAgICAgICAgICAgcm9sZWJldCA9ICJIaSINCiAgICAgICAgICAgICAgICAgIG5vX3JvbGViZXQgPSAwDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICByb2xlYmV0ID0gb2JqWyJDb25maWciXVt1cnV0XVsiQmV0Il1bIkJldCJdDQogICAgICAgIGlmIG15X25hbWVzcGFjZS5iZXRzZXQgPT0gIkF1dG8iIG9yIG15X25hbWVzcGFjZS5iZXRzZXQgPT0gIkFVVE8iIG9yIG15X25hbWVzcGFjZS5iZXRzZXQgPT0gImF1dG8iOg0KICAgICAgICAgIHdha3R1ID0gZGF0ZXRpbWUubm93KCkuc3RyZnRpbWUoJyVNJykNCiAgICAgICAgICBpZiBpbnQod2FrdHUpID4gaW50KG1lbml0IC0gMSk6DQogICAgICAgICAgICAgbWVuaXQgPSBpbnQobWVuaXQpICsgaW50KG9ialsiSW50ZXJ2YWwiXSkNCiAgICAgICAgICAgICB1cnV0ICs9MQ0KICAgICAgICAgICAgIGlmIHVydXQgPT0ganVtbGFodWxhbmc6DQogICAgICAgICAgICAgICAgdXJ1dCA9IDANCiAgICAgICAgICAgICBwcmludCAoIkNoYW5nZSBCZXQgU2V0ICIrb2JqWyJDb25maWciXVt1cnV0XVsiTmFtZSBCZXQgU2V0Il0rIiAgICAgICAgICAgICAgICAgICAgICAgICAgICIpDQogICAgICAgICAgICAgc2xwID0gaW50KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkludGVydmFsIl0pIC8gMTAwMA0KICAgICAgICAgICAgIGxpbWl0X2EgPSBpbnQob2JqWyJDb25maWciXVt1cnV0XVsiUmVzZXQgSWYgV2luIl0pIC0gMQ0KICAgICAgICAgICAgIHBheWluID0gaW50KGZsb2F0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkJhc2UgQmV0Il0pKigxMCAqKiA4KSkNCiAgICAgICAgICAgICBhbW91bnQgPSBwYXlpbg0KDQogICAgICAgIGVsc2U6DQogICAgICAgICAgdXJ1dCA9IGludChteV9uYW1lc3BhY2UuYmV0c2V0KQ0KDQogICAgICAgIGlmIG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJhbmRvbSBDaGFuY2UiXVsiVG9nZ2xlIl0gPT0gIk9OIiBvciBvYmpbIkNvbmZpZyJdW3VydXRdWyJSYW5kb20gQ2hhbmNlIl1bIlRvZ2dsZSJdID09ICJPbiIgb3Igb2JqWyJDb25maWciXVt1cnV0XVsiUmFuZG9tIENoYW5jZSJdWyJUb2dnbGUiXSA9PSAib24iOg0KICAgICAgICAgICBoYXNpbF9jaGFuY2UgPSByb3VuZChyYW5kb20udW5pZm9ybShmbG9hdChvYmpbIkNvbmZpZyJdW3VydXRdWyJSYW5kb20gQ2hhbmNlIl1bIk1pbiJdKSxmbG9hdChvYmpbIkNvbmZpZyJdW3VydXRdWyJSYW5kb20gQ2hhbmNlIl1bIk1heCJdKSksMikNCiAgICAgICAgICAgY29rID0gbGVuKHN0cihoYXNpbF9jaGFuY2UpKQ0KICAgICAgICAgICBpZiBjb2sgPT0gMzoNCiAgICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHIiK3N0cihoYXNpbF9jaGFuY2UpKyIgICAiKQ0KICAgICAgICAgICBpZiBjb2sgPT0gNDoNCiAgICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHIiK3N0cihoYXNpbF9jaGFuY2UpKyIgICIpDQogICAgICAgICAgIGlmIGNvayA9PSA1Og0KICAgICAgICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKCJcciIrc3RyKGhhc2lsX2NoYW5jZSkrIiAiKQ0KICAgICAgICAgICBrb252ZXJ0KGhhc2lsX2NoYW5jZSxzdHIocm9sZWJldCkpDQogICAgICAgIGVsc2U6DQogICAgICAgICAgIGtvbnZlcnQob2JqWyJDb25maWciXVt1cnV0XVsiQ2hhbmNlIl0sc3RyKHJvbGViZXQpKQ0KDQogICAgICAgIHRpbWUuc2xlZXAoZmxvYXQoc2xwKSkNCiAgICAgICAgYW1vdW50ID0gaW50KGFtb3VudCkNCiAgICAgICAgbis9MQ0KICAgICAgICBkYXRhID0gew0KICAgICAgICAgICJhIjogIlBsYWNlQmV0IiwNCiAgICAgICAgICAicyI6IGpzWyJTZXNzaW9uQ29va2llIl0sDQogICAgICAgICAgIlBheUluIjogYW1vdW50LA0KICAgICAgICAgICJMb3ciOiBsb3csDQogICAgICAgICAgIkhpZ2giOiBoaWdoLA0KICAgICAgICAgICJDbGllbnRTZWVkIjogcmFuZGludCgwLDk5OTk5OSksDQogICAgICAgICAgIkN1cnJlbmN5IjogImRvZ2UiLA0KICAgICAgICAgICJQcm90b2NvbFZlcnNpb24iOiAiMiINCiAgICAgICAgfQ0KICAgICAgICBpZiBwcm9mID4gZmxvYXQob2JqWyJUYXJnZXQgUHJvZml0Il0pOg0KICAgICAgICAgICBwcmludCAoaGlqYXUrIlxuWWF5LiEgXG5Qcm9maXQgTWVuY2FwYWkgVGFyZ2V0Li4uLi4hXG4iK2hpamF1KyJQcm9maXQgIityZXMrc3RyKHByb2YpKQ0KICAgICAgICAgICBvcy5zeXN0ZW0oInRlcm11eC10b2FzdCBZb3Ugd2luICIrc3RyKHByb2YpKQ0KICAgICAgICAgICB0aW1lLnNsZWVwKDEpDQogICAgICAgICAgIG9zLnN5c3RlbSgidGVybXV4LXRvYXN0IFRvdGFsIEJhbGFuY2UgIitzdHIoZmxvYXQoaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkpLygxMCAqKiA4KSkpDQogICAgICAgICAgIHN5cy5leGl0KCkNCiAgICAgICAgcjEgPSBjLnBvc3QodXJsLGhlYWRlcnM9dWEsZGF0YT1kYXRhKQ0KICAgICAgICBqc24gPSBqc29uLmxvYWRzKHIxLnRleHQpDQogICAgICAgIHByb2YgPSAoZmxvYXQoanNuWyJTdGFydGluZ0JhbGFuY2UiXSArIGludChqc25bIlBheU91dCJdKSAtIGludChhbW91bnQpIC0ganVtYmwpLygxMCAqKiA4KSkNCiAgICAgICAganVtID0gaW50KGpzblsiUGF5T3V0Il0pIC0gaW50KGFtb3VudCkNCiAgICAgICAgaWYganNuWyJTdGFydGluZ0JhbGFuY2UiXSA+IHdzOg0KICAgICAgICAgICBwcmludCAodW5ndSsiWyIrcmVzK3N0cihyb2xlYmV0KSt1bmd1KyJdICIraGlqYXUyK3N0cihmbG9hdChhbW91bnQpLygxMCAqKiA4KSkscmVzK3N0cihmbG9hdChpbnQoanNuWyJTdGFydGluZ0JhbGFuY2UiXSkgKyBpbnQoanVtKSkvKDEwICoqIDgpKSxoaWphdTIrIlByb2ZpdCIscmVzK3N0cihwcm9mKSkNCiAgICAgICAgICAgcHJpbnQgKGhpamF1KyJZYXkuIVxuQmFsYW5jZSBTdWRhaCBNZW1lbnVoaSBUYXJnZXQuLi4uLiEiKQ0KICAgICAgICAgICBvcy5zeXN0ZW0oInRlcm11eC10b2FzdCBUYXJnZXQgV2luIFN1ZGFoIFRlcmNhcGFpIikNCiAgICAgICAgICAgdGltZS5zbGVlcCgxKQ0KICAgICAgICAgICBvcy5zeXN0ZW0oInRlcm11eC10b2FzdCBUb3RhbCBCYWxhbmNlICIrc3RyKGZsb2F0KGludChqc25bIlN0YXJ0aW5nQmFsYW5jZSJdKSArIGludChqdW0pKS8oMTAgKiogOCkpKQ0KICAgICAgICAgICBzeXMuZXhpdCgpDQogICAgICAgIGlmIGpzblsiU3RhcnRpbmdCYWxhbmNlIl0gPCBsczoNCiAgICAgICAgICAgcHJpbnQgKHVuZ3UrIlsiK3JlcytzdHIocm9sZWJldCkrdW5ndSsiXSIrcmVkMisiLSIrc3RyKGZsb2F0KGFtb3VudCkvKDEwICoqIDgpKSxyZXMrc3RyKChmbG9hdChpbnQoanNuWyJTdGFydGluZ0JhbGFuY2UiXSkgKyBpbnQoanVtKSkvKDEwICoqIDgpKSkscmVkMisiTG9zZSAiLHJlcytzdHIocHJvZikpDQogICAgICAgICAgIHByaW50IChTdHlsZS5CUklHSFQrRm9yZS5SRUQrIkxvc2UgVGFyZ2V0Li4uLiEiKQ0KICAgICAgICAgICBvcy5zeXN0ZW0oInRlcm11eC10b2FzdCBMb3NlIFRhcmdldCAiKQ0KICAgICAgICAgICB0aW1lLnNsZWVwKDEpDQogICAgICAgICAgIG9zLnN5c3RlbSgidGVybXV4LXRvYXN0IFRvdGFsIEJhbGFuY2UgIitzdHIoZmxvYXQoaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkpLygxMCAqKiA4KSkpDQogICAgICAgICAgIHN5cy5leGl0KCkNCiAgICAgICAgaWYganNuWyJQYXlPdXQiXSBpcyBub3QgMDoNCiAgICAgICAgICAgbm9fd2luICs9MQ0KICAgICAgICAgICBub19sb3NlID0gMA0KICAgICAgICAgICBiYWwgPSBpbnQoanNuWyJTdGFydGluZ0JhbGFuY2UiXSkgKyBpbnQoanVtKQ0KICAgICAgICAgICBpZiBwcm9mID4gMDoNCiAgICAgICAgICAgICBwcmludCAodW5ndSsiWyIrcmVzK3N0cihyb2xlYmV0KSt1bmd1KyJdICIraGlqYXUyK3N0cihyZXYoc3RyKGFtb3VudCkpKSxyZXMrc3RyKHJldihzdHIoYmFsKSkpLGhpamF1MisiUHJvZml0IixyZXMrc3RyKHByb2YpKQ0KICAgICAgICAgICBlbHNlOg0KICAgICAgICAgICAgIHByaW50ICh1bmd1KyJbIityZXMrc3RyKHJvbGViZXQpK3VuZ3UrIl0gIitoaWphdTIrc3RyKHJldihzdHIoYW1vdW50KSkpLHJlcytzdHIocmV2KHN0cihiYWwpKSkscmVkMisiTG9zZSAiLHJlcytzdHIocHJvZikpDQogICAgICAgICAgIGFtb3VudCA9IGludChhbW91bnQpICogZmxvYXQob2JqWyJDb25maWciXVt1cnV0XVsiSWYgV2luIl0pDQoNCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgbm9fd2luID0gMA0KICAgICAgICAgICBub19sb3NlICs9MQ0KICAgICAgICAgICBpID0gMA0KICAgICAgICAgICBidXJzdCA9IFRydWUNCiAgICAgICAgICAgYmFsID0gaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkNCiAgICAgICAgICAgaWYgcHJvZiA+IDA6DQogICAgICAgICAgICAgcHJpbnQgKHVuZ3UrIlsiK3JlcytzdHIocm9sZWJldCkrdW5ndSsiXSIrcmVkMisiLSIrc3RyKHJldihzdHIoYW1vdW50KSkpLHJlcytzdHIocmV2KHN0cihiYWwpKSksaGlqYXUyKyJQcm9maXQiLHJlcytzdHIocHJvZikpDQogICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgcHJpbnQgKHVuZ3UrIlsiK3JlcytzdHIocm9sZWJldCkrdW5ndSsiXSIrcmVkMisiLSIrc3RyKHJldihzdHIoYW1vdW50KSkpLHJlcytzdHIocmV2KHN0cihiYWwpKSkscmVkMisiTG9zZSAiLHJlcytzdHIocHJvZikpDQogICAgICAgICAgIGFtb3VudCA9IGludChhbW91bnQpICogZmxvYXQob2JqWyJDb25maWciXVt1cnV0XVsiSWYgTG9zZSJdKQ0KICAgICAgICBpZiBzdGF0c19pZl9wcm9maXQgaXMgVHJ1ZToNCiAgICAgICAgICAgIGlmIHByb2YgPiBmbG9hdChyZXNldF9pZl9wcm9maXQpOg0KICAgICAgICAgICAgICAgYW1vdW50ID0gcGF5aW4NCiAgICAgICAgICAgICAgIHJlc2V0X2lmX3Byb2ZpdCA9IGZsb2F0KHByb2YpK2Zsb2F0KHRvdF9pZl9wcm9maXQpDQoNCiAgICAgICAgaWYgYnVyc3QgaXMgVHJ1ZToNCiAgICAgICAgICAgaSs9MQ0KICAgICAgICAgICBpZiBpID4gbGltaXRfYToNCiAgICAgICAgICAgICBpID0gMA0KICAgICAgICAgICAgIGJ1cnN0ID0gRmFsc2UNCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgaWYgbiA+IGxpbWl0X2E6DQogICAgICAgICAgICAgbiA9IDANCiAgICAgICAgICAgICBhbW91bnQgPSBwYXlpbg0KDQogICAgICAgIGlmIG5vX3dpbiA+IHRvdGFsX3dpbjoNCiAgICAgICAgICAgc3RhdHNfcm9sZWJldF93aW4gPSBUcnVlDQogICAgICAgICAgIHN0YXRzX3JvbGViZXRfbG9zZSA9IEZhbHNlDQogICAgICAgICAgIHRvdGFsX3dpbiArPTENCiAgICAgICAgaWYgbm9fbG9zZSA+IHRvdGFsX2xvc2U6DQogICAgICAgICAgIHN0YXRzX3JvbGViZXRfbG9zZSA9IFRydWUNCiAgICAgICAgICAgc3RhdHNfcm9sZWJldF93aW4gPSBGYWxzZQ0KICAgICAgICAgICB0b3RhbF9sb3NlICs9MQ0KICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKGhpamF1KyIgICAgICAgIFdpbiBTdHJlYWsgIityZXMrc3RyKHRvdGFsX3dpbikrcmVkKyIgTG9zZSBTdHJlYWsgIityZXMrc3RyKHRvdGFsX2xvc2UpKyJcciIpDQogICAgICAgIGlmIG9ialsiQXV0byBXZCJdWyJUb2dnbGUiXSA9PSAiT24iIG9yIG9ialsiQXV0byBXZCJdWyJUb2dnbGUiXSA9PSAiT04iIG9yIG9ialsiQXV0byBXZCJdWyJUb2dnbGUiXSA9PSAib24iOg0KICAgICAgICAgICBpZiBmbG9hdChyZXYoc3RyKGJhbCkpKSA+IGZsb2F0KG9ialsiQXV0byBXZCJdWyJJZiBCYWxhbmNlIl0pOg0KICAgICAgICAgICAgICB3ZCA9IHsNCiAgICAgICAgICAgICAgICAiYSI6ICJXaXRoZHJhdyIsDQogICAgICAgICAgICAgICAgInMiOiBqc1siU2Vzc2lvbkNvb2tpZSJdLA0KICAgICAgICAgICAgICAgICJBbW91bnQiOiBpbnQoZmxvYXQob2JqWyJBdXRvIFdkIl1bIkFtb3VudCJdKSooMTAgKiogOCkpLA0KICAgICAgICAgICAgICAgICJBZGRyZXNzIjogb2JqWyJBdXRvIFdkIl1bIldhbGxldCBBZGRyZXNzIl0sDQogICAgICAgICAgICAgICAgIlRvdHAiOiAiIiwNCiAgICAgICAgICAgICAgICAiQ3VycmVuY3kiOiAiZG9nZSINCg0KICAgICAgICAgICAgICB9DQogICAgICAgICAgICAgIHIxID0gYy5wb3N0KHVybCxoZWFkZXJzPXVhLGRhdGE9d2QpDQogICAgICAgICAgICAgIHdpdGhkcmF3ID0ganNvbi5sb2FkcyhyMS50ZXh0KQ0KICAgICAgICAgICAgICBwcmludCAoIiIpDQogICAgICAgICAgICAgIHByaW50ICgiV2l0aGRyYXcgIitzdHIocmV2KHN0cih3aXRoZHJhd1siUGVuZGluZyJdKSkpKQ0KICAgICAgICAgICAgICB3aXRoIG9wZW4oImhpc3RvcnkubG9nIiwiYSsiKSBhcyBmOg0KICAgICAgICAgICAgICAgICAgZi53cml0ZSgiV2l0aGRyYXcgIitzdHIocmV2KHN0cih3aXRoZHJhd1siUGVuZGluZyJdKSkpKyJcbiIpDQogICAgICAgICAgICAgIHN5cy5leGl0KCkNCg0KDQoNCiAgIGV4Y2VwdDoNCiAgICAgICBwcmludCAoIiIpDQogICAgICAgb3Muc3lzdGVtKCJ0ZXJtdXgtdG9hc3QgQmV0dGluZyBTdG9wIikNCiAgICAgICB0cnk6DQogICAgICAgICAgd2l0aCBvcGVuKCJoaXN0b3J5LmxvZyIsImErIikgYXMgZjoNCiAgICAgICAgICAgICAgZi53cml0ZSgiWyIrZGF0ZXRpbWUubm93KCkuc3RyZnRpbWUoJyVZLyVtLyVkICVIOiVNOiVTJykrIl0gV2luIFN0cmVhayAiK3N0cih0b3RhbF93aW4pKyIgTG9zZSBTdHJlYWsgIitzdHIodG90YWxfbG9zZSkrIiB8IEJhbGFuY2UgIitzdHIoZmxvYXQoaW50KGpzblsiU3RhcnRpbmdCYWxhbmNlIl0pICsgaW50KGp1bSkpLygxMCAqKiA4KSkrIiBQcm9maXQgIitzdHIocHJvZikrIlxuIikNCiAgICAgICBleGNlcHQ6DQogICAgICAgICAgcHJpbnQgKHJlZDIrIkJhbGFuY2UgTm90IEVub3VnaCIpDQogICAgICAgc3lzLmV4aXQoKQ0KciA9IGMuZ2V0KHVybCxoZWFkZXJzPXVhLGRhdGE9eyJhIjogIkxvZ2luIiwiS2V5IjogIjdlYzdmOGEyYzk3MjRiMmNiYjhlZDc1ZTcyYjQ3ZWU5IiwiVXNlcm5hbWUiOiBvYmpbIkFjY291bnQiXVsiVXNlcm5hbWUiXSwiUGFzc3dvcmQiOiBvYmpbIkFjY291bnQiXVsiUGFzc3dvcmQiXSwiVG90cCI6ICIifSkNCmpzID0ganNvbi5sb2FkcyhyLnRleHQpDQp0cnk6DQogIHByaW50IChoaWphdSsiQmFsYW5jZSAiK2FidTIrIjogIityZXMrc3RyKGZsb2F0KGpzWyJEb2dlIl1bIkJhbGFuY2UiXSkvKDEwICoqIDgpKSkNCmV4Y2VwdDoNCiAgcHJpbnQgKCJDaGVjayBZb3VyIFVzZXJuYW1lIEFuZCBZb3VyIFBhc3N3b3JkIikNCiAgc3lzLmV4aXQoKQ0KDQoNCmRpY2UoaW50KGZsb2F0KG9ialsiVGFyZ2V0IFdpbiJdKSooMTAgKiogOCkpLGludChmbG9hdChvYmpbIkxvc2UgVGFyZ2V0Il0pKigxMCAqKiA4KSkp"))
