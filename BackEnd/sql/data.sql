USE [trac_nghiem]
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'k4BYaYk7', N'teacher1@gmail.com', N'Đặng Hoài Phương', N'$2b$12$vRAvt7uiYPCmpf79FrzuAuXbO6yctv76uNhIa80i4vgzvVpUy4hQa', N'Teacher\k4BYaYk7\Avatar\k4BYaYk7.webp', 0, CAST(N'2024-04-09T21:23:09.543' AS DateTime), 0)
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'OStVxHm4', N'teacher4@gmail.com', N'Ninh Khánh Duy', N'$2b$12$21td84zi.DPLLuz0g6F5weOLt5yrTan1Rxk4flfkRVQsgY.ZZ6ZP.', NULL, 0, CAST(N'2024-04-11T19:00:26.570' AS DateTime), 0)
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'qdj0IvKj', N'teacher3@gmail.com', N'Đặng Hoài Phương', N'$2b$12$7ykZao.Frb5AQ3oPTF8XA.27ScWuq0roZkR.YcJUn1vOwwskIuel2', NULL, 0, CAST(N'2024-04-11T19:00:16.653' AS DateTime), 0)
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'vHe3zIzf', N'teacher2@gmail.com', N'Võ Đức Hoàng', N'$2b$12$Gkph6kaLr6.Bi2WfjG/tuuDuL1apWsfV0Fa8nn3FYB.O/eaXZpNLC', NULL, 0, CAST(N'2024-04-11T19:00:04.087' AS DateTime), 0)
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'XmzWcIt6', N'teacher5@gmail.com', N'Hishinuma Takeru', N'$2b$12$fk9rP7TyVPRbEn0eH/tCcey3NdsDZs.kEzXpwbeDC3dIvubU1FPau', NULL, 0, CAST(N'2024-04-11T19:00:50.403' AS DateTime), 0)
GO
INSERT [dbo].[teacher] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'zMqDbgtI', N'teacher6@gmail.com', N'Hishinuma Takeru', N'$2b$12$N./lmpz9DrIR2.iwEpOvY.hVViwLq0eXlw/Up3OF7t6SJzjZ.jYe6', NULL, 0, CAST(N'2024-04-20T00:10:01.920' AS DateTime), 0)
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'0xWn65Yh', N'k4BYaYk7', N'Lập trình 1v1', CAST(N'2024-04-20T00:20:36.567' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'1tgJhUnW', N'k4BYaYk7', N'Tiếng Nhật 6', CAST(N'2024-04-27T11:08:26.297' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'6d789LoC', N'k4BYaYk7', N'Lập trình pypy', CAST(N'2024-04-13T21:42:13.180' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'kNEoTGIA', N'k4BYaYk7', N'Lập trình Java', CAST(N'2024-04-13T21:42:26.840' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'OeLujW1I', N'k4BYaYk7', N'Lập trình C#', CAST(N'2024-04-13T21:42:22.117' AS DateTime))
GO
INSERT [dbo].[collection] ([id], [teacher_id], [name], [created_timestamp]) VALUES (N'tSwFdgXT', N'k4BYaYk7', N'Lập trình mạng', CAST(N'2024-04-13T21:42:30.320' AS DateTime))
GO
INSERT [dbo].[test] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'NozNAvgG', N'6d789LoC', N'Kiểm tra cuối kỳ lập trình java', CAST(N'2024-05-03T22:14:12.930' AS DateTime))
GO
INSERT [dbo].[test] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'r7TFxgap', N'6d789LoC', N'Kiểm tra giữa kỳ', CAST(N'2024-05-03T22:11:15.093' AS DateTime))
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'4wFJBkca', N'GROUP 4', N'k4BYaYk7', CAST(N'2024-04-09T21:23:41.970' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'88lE7JMs', N'NHÓM 3', N'vHe3zIzf', CAST(N'2024-04-11T19:03:41.667' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'8KV9eD8t', N'GROUP 1', N'k4BYaYk7', CAST(N'2024-04-09T21:23:32.020' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'BWHlJddv', N'NHÓM 21.13', N'qdj0IvKj', CAST(N'2024-04-11T19:05:43.163' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'cdSUupLc', N'21TCLC_Nhat1', N'k4BYaYk7', CAST(N'2024-04-09T21:23:43.800' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'ch0RHd4F', N'GROUP 3', N'k4BYaYk7', CAST(N'2024-04-09T21:23:39.930' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'DiCEH2as', N'NHÓM 6', N'vHe3zIzf', CAST(N'2024-04-11T19:03:54.487' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'e73BTGJF', N'NHÓM 21.16', N'k4BYaYk7', CAST(N'2024-04-20T00:15:14.810' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'F4yxaXa2', N'NHÓM 5', N'vHe3zIzf', CAST(N'2024-04-11T19:03:46.793' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'H2hL5gmR', N'NHÓM 8', N'vHe3zIzf', CAST(N'2024-04-11T19:03:58.080' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'hJhx5jDm', N'NHÓM 2', N'vHe3zIzf', CAST(N'2024-04-11T19:03:39.230' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'KTwfIxXF', N'NHÓM 7', N'vHe3zIzf', CAST(N'2024-04-11T19:03:56.277' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'MgbsLHP3', N'GROUP 9', N'k4BYaYk7', CAST(N'2024-04-09T21:23:53.343' AS DateTime), 0)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'mjuZ72rB', N'NHÓM 21.14', N'qdj0IvKj', CAST(N'2024-04-11T19:05:46.250' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'ohIym4EM', N'NHÓM 2', N'k4BYaYk7', CAST(N'2024-04-11T19:02:55.557' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'okwqEGLO', N'GROUP 10', N'k4BYaYk7', CAST(N'2024-04-09T21:23:57.223' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'PzZJoaTL', N'GROUP 6', N'k4BYaYk7', CAST(N'2024-04-09T21:23:46.017' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'QgB3WvKg', N'GROUP 2', N'k4BYaYk7', CAST(N'2024-04-09T21:23:37.807' AS DateTime), 0)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'qJyDN6Nj', N'NHÓM 21.12', N'qdj0IvKj', CAST(N'2024-04-11T19:05:38.470' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'tqiOBYQR', N'GROUP 7', N'k4BYaYk7', CAST(N'2024-04-09T21:23:47.683' AS DateTime), 0)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'tU7Z7LzW', N'NHÓM 3', N'k4BYaYk7', CAST(N'2024-04-11T19:02:57.997' AS DateTime), 0)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'uxpWkXSK', N'NHÓM 4', N'vHe3zIzf', CAST(N'2024-04-11T19:03:44.290' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'uzKPouin', N'NHÓM 1', N'k4BYaYk7', CAST(N'2024-04-11T19:02:52.893' AS DateTime), 0)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'vKKOhuV5', N'NHÓM 21.16', N'qdj0IvKj', CAST(N'2024-04-11T19:05:56.537' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'X7DytzIM', N'NHÓM 21.15', N'qdj0IvKj', CAST(N'2024-04-11T19:05:49.610' AS DateTime), 1)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'yzzd7zkN', N'GROUP 8', N'k4BYaYk7', CAST(N'2024-04-09T21:23:49.953' AS DateTime), 0)
GO
INSERT [dbo].[group] ([id], [name], [teacher_id], [created_timestamp], [is_show]) VALUES (N'ZR9t9Jjv', N'NHÓM 1', N'vHe3zIzf', CAST(N'2024-04-11T19:03:36.220' AS DateTime), 1)
GO
INSERT [dbo].[group_test] ([id], [group_id], [test_id], [start], [end], [created_timestamp], [duration], [shuffle]) VALUES (N'rV8HKzdz', N'uzKPouin', N'NozNAvgG', CAST(N'2024-05-10T09:30:00.000' AS DateTime), CAST(N'2024-05-10T11:30:00.000' AS DateTime), CAST(N'2024-05-04T13:12:30.400' AS DateTime), 40, 0)
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'cc2Gwojy', N'1tgJhUnW', N'Đọc hiểu', CAST(N'2024-04-27T11:09:23.600' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'DWmNYB3t', N'6d789LoC', N'Chương 1: Python Object and Data Structure', CAST(N'2024-04-13T21:46:10.920' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'Ff2II1ZI', N'1tgJhUnW', N'Nghe hiểu', CAST(N'2024-04-27T11:09:28.900' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'fIe2sf0n', N'6d789LoC', N'Chương 4', CAST(N'2024-04-13T21:53:20.143' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'JRlaw4RT', N'1tgJhUnW', N'Hán tự', CAST(N'2024-04-27T11:09:18.440' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'RqOBnbVT', N'6d789LoC', N'Chương 2', CAST(N'2024-04-13T21:53:15.363' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'TaOqAVbD', N'1tgJhUnW', N'Từ vựng', CAST(N'2024-04-27T11:09:08.647' AS DateTime))
GO
INSERT [dbo].[question_bank] ([id], [collection_id], [name], [created_timestamp]) VALUES (N'U7X5Denq', N'6d789LoC', N'Chương 3', CAST(N'2024-04-13T21:53:18.030' AS DateTime))
GO
INSERT [dbo].[test_structure] ([test_id], [question_bank_id], [number_of_question]) VALUES (N'r7TFxgap', N'cc2Gwojy', 0x80049553000000000000005D94287D94288C0A646966666963756C7479944B018C126E756D6265725F6F665F7175657374696F6E944B01757D942868024B0268034B01757D942868024B0368034B01757D942868024B0468034B0175652E)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'8iOZNT4P', N'student1@gmail.com', N'Goku', N'$2b$12$ipEFqoWa8j2SOg00GI4WKekmU92T/JI6yN6TmHEVB1PIfO39Ok3o6', N'Student\8iOZNT4P\Avatar\8iOZNT4P.webp', 0, CAST(N'2024-04-09T21:24:09.537' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'NkvFWLYJ', N'student8@gmail.com', N'Học sinh 8', N'$2b$12$AF8n2CDmzTKOlt6DdzPC2uVIxGud9H4H4Y3oQIobw/Jecq5mZRs4O', NULL, 0, CAST(N'2024-04-09T21:24:40.797' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'olF2PEiv', N'student4@gmail.com', N'Học sinh 4', N'$2b$12$lTEG7fcENFpnDsv9Tvc8luDkH8MiDHVARWE4u8c2pIXqqpbRYzQoK', NULL, 0, CAST(N'2024-04-09T21:24:22.130' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'qVcy54uO', N'student5@gmail.com', N'Học sinh 5', N'$2b$12$oQa66pl6RkFo2q4bMT6FludvgxaAsfyUZf72vFRxH3YQhxB74YgDG', NULL, 0, CAST(N'2024-04-09T21:24:26.060' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'SlW241eT', N'student9@gmail.com', N'Học sinh 9', N'$2b$12$rmzWumCZ/FGXeDyaTYpNueX5mmzb3VCoeTCfcM0puD3Z4eXOjB26q', NULL, 0, CAST(N'2024-04-09T21:24:45.250' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'Tj2WdsIk', N'student10@gmail.com', N'Học sinh 10', N'$2b$12$/ncUjvvpPOllKU9dB/9KZe7Bc9VPIsI3ziLQ5dw16b0BxYRRmBO0W', NULL, 0, CAST(N'2024-04-09T21:24:51.960' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'vAN0Ef2M', N'student6@gmail.com', N'Học sinh 6', N'$2b$12$4foUvTAjgSuILq/wd9ffdekuUh7YOB3.ZTm24rz9Gw2xMrPu4Gl2O', NULL, 0, CAST(N'2024-04-09T21:24:31.320' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'VoJY8oV3', N'student2@gmail.com', N'Học sinh 2', N'$2b$12$pEvbcDxT6G.dV1Qpwb.7X.xfr3SsTBRLBX2Xeo0CWeYNQ8jeP54CW', NULL, 0, CAST(N'2024-04-09T21:24:13.717' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'vwRhDHHL', N'student3@gmail.com', N'Học sinh 3', N'$2b$12$65v2uH4mVXvNTFcyi38zuOYGzXt8JXcy9dwSD9BenHP/E97o15K0W', NULL, 0, CAST(N'2024-04-09T21:24:17.667' AS DateTime), 0)
GO
INSERT [dbo].[student] ([id], [email], [name], [hash_pswd], [avatar_path], [is_banned], [created_timestamp], [is_verified]) VALUES (N'Z7cJJrs1', N'student7@gmail.com', N'Học sinh 7', N'$2b$12$ZEhH2eHFlH9MYSGdc3CIfucb.dPgQT9Uf3G6t4kaMEmaw6In/YqSe', NULL, 0, CAST(N'2024-04-09T21:24:35.977' AS DateTime), 0)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'4wFJBkca', N'8iOZNT4P', 1, CAST(N'2024-04-12T17:30:21.940' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'4wFJBkca', N'NkvFWLYJ', 1, CAST(N'2024-04-12T17:30:21.963' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'4wFJBkca', N'olF2PEiv', 1, CAST(N'2024-04-12T17:30:21.987' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'88lE7JMs', N'8iOZNT4P', 1, CAST(N'2024-04-11T20:04:38.593' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'88lE7JMs', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.850' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:40:56.223' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'olF2PEiv', 0, CAST(N'2024-04-11T20:40:56.230' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'qVcy54uO', 0, CAST(N'2024-04-11T20:40:56.230' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'SlW241eT', 0, CAST(N'2024-04-11T20:40:56.237' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'cdSUupLc', N'Tj2WdsIk', 0, CAST(N'2024-04-11T20:40:56.240' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'DiCEH2as', N'8iOZNT4P', 1, CAST(N'2024-04-11T20:04:47.683' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'DiCEH2as', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.860' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'F4yxaXa2', N'8iOZNT4P', 0, CAST(N'2024-04-11T20:04:51.653' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'F4yxaXa2', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.863' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'H2hL5gmR', N'8iOZNT4P', 0, CAST(N'2024-04-11T20:04:57.803' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'H2hL5gmR', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.867' AS DateTime), 1)
GO
INSERT [dbo].[group_student] ([group_id], [student_id], [is_join], [request_timestamp], [is_show]) VALUES (N'vKKOhuV5', N'NkvFWLYJ', 0, CAST(N'2024-04-11T20:07:00.870' AS DateTime), 1)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'f3bdcs483T', N'cc2Gwojy', -32767, N'', 0x8004954C000000000000005D94287D94288C07636F6E74656E74948C0131948C0A69735F636F72726563749489757D942868028C013294680489757D942868028C013394680488757D942868028C01349468048975652E, 1, 0x8004955F000000000000005D948C58546561636865725C6B34425961596B375C436F6C6C656374696F6E5C3174674A68556E575C5175657374696F6E42616E6B5C63633247776F6A795C5175657374696F6E5C663362646373343833545C4A386E4E702E706E6794612E)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'H1lVqWxo8W', N'RqOBnbVT', -32768, N'Which of the following is the correct extension of the Python file?', 0x80049557000000000000005D94287D94288C07636F6E74656E74948C072E707974686F6E948C0A69735F636F72726563749489757D942868028C032E706C94680489757D942868028C032E707994680488757D942868028C022E709468048975652E, 1, 0x800495BB000000000000005D94288C58546561636865725C6B34425961596B375C436F6C6C656374696F6E5C36643738394C6F435C5175657374696F6E42616E6B5C52714F426E6256545C5175657374696F6E5C48316C567157786F38575C78423651502E706E67948C58546561636865725C6B34425961596B375C436F6C6C656374696F6E5C36643738394C6F435C5175657374696F6E42616E6B5C52714F426E6256545C5175657374696F6E5C48316C567157786F38575C334469484D2E6D703394652E)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'OnOsbRUo1L', N'RqOBnbVT', -32765, N'<p>What will be the value of the following Python expression?</p><code>4 + 3 % 5</code>', 0x8004954C000000000000005D94287D94288C07636F6E74656E74948C0137948C0A69735F636F72726563749488757D942868028C013294680489757D942868028C013494680489757D942868028C01319468048975652E, 1, NULL)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'Q1SjGgdY1G', N'cc2Gwojy', -32768, N'', 0x8004954C000000000000005D94287D94288C07636F6E74656E74948C0131948C0A69735F636F72726563749489757D942868028C013294680489757D942868028C013394680488757D942868028C01349468048975652E, 1, NULL)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'RN3YUyCVv8', N'RqOBnbVT', -32767, N'Is Python code compiled or interpreted?', 0x800495DE000000000000005D94287D94288C07636F6E74656E74948C2C507974686F6E20636F646520697320626F746820636F6D70696C656420616E6420696E746572707265746564948C0A69735F636F72726563749488757D942868028C2F507974686F6E20636F6465206973206E65697468657220636F6D70696C6564206E6F7220696E74657270726574656494680489757D942868028C1C507974686F6E20636F6465206973206F6E6C7920636F6D70696C656494680489757D942868028C1F507974686F6E20636F6465206973206F6E6C7920696E7465727072657465649468048975652E, 1, 0x800495BB000000000000005D94288C58546561636865725C6B34425961596B375C436F6C6C656374696F6E5C36643738394C6F435C5175657374696F6E42616E6B5C52714F426E6256545C5175657374696F6E5C524E33595579435676385C57324956492E706E67948C58546561636865725C6B34425961596B375C436F6C6C656374696F6E5C36643738394C6F435C5175657374696F6E42616E6B5C52714F426E6256545C5175657374696F6E5C524E33595579435676385C704D6865622E6D703394652E)
GO
INSERT [dbo].[question] ([id], [question_bank_id], [order_number], [content], [answer], [difficulty], [attachment]) VALUES (N'UNhUnLVfTm', N'RqOBnbVT', -32766, N'All keywords in Python are in _________', 0x8004957C000000000000005D94287D94288C07636F6E74656E74948C0B4361706974616C697A6564948C0A69735F636F72726563749489757D942868028C0A6C6F776572206361736594680489757D942868028C0A5550504552204341534594680489757D942868028C154E6F6E65206F6620746865206D656E74696F6E65649468048875652E, 2, NULL)
GO
