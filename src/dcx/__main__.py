const_epilog = "CgpNQU5VQUwKCgoKMS4gR0VUVElORyBTVEFSVEVECi4uIDEuIElOU1RBTExBVElPTgouLi4uLiAxLiBXaW5kb3dzCi4uIDIuIFBPU1QtSU5TVEFMTEFUSU9OCi4uIDMuIFdPUktGTE9XIERFRklOSVRJT04gRk9STUFUCi4uLi4uIDEuIERJUkVDVE9SWSBTVFJVQ1RVUkUKLi4uLi4gMi4gRklMRSBGT1JNQVQKLi4uLi4gMy4gTUlOSU1BTCBFWEFNUExFIGBwbGF5LmpzJwouLiA0LiBDUkVBVEUgTkVXIFdPUktGTE9XCi4uIDUuIFJVTiBUSEUgTkVXIFdPUktGTE9XCi4uIDYuIERJUkVDVE9SWSBgbG9nJyBBRlRFUiBFWEVDVVRJT04KMi4gQ09NTUFORCBSRUZFUkVOQ0UKLi4gMS4gT1ZFUlZJRVcKCgoKCgoxIEdFVFRJTkcgU1RBUlRFRAo9PT09PT09PT09PT09PT09PQoKMS4xIElOU1RBTExBVElPTgp+fn5+fn5+fn5+fn5+fn5+CgoxLjEuMSBXaW5kb3dzCi0tLS0tLS0tLS0tLS0KCiAgSW5zdGFsbCBhIHJlY2VudCBgcHl0aG9uMycgKExUUyByZWxlYXNlcyByZWNvbW1lbmRlZCBmcm9tIHRoZSBvcmlnaW5hbAogIHdlYnNpdGUgPGh0dHBzOi8vd3d3LnB5dGhvbi5vcmcvZG93bmxvYWRzL3dpbmRvd3MvPikgYW5kIHJ1biBgcGlwCiAgaW5zdGFsbCBkY3gnIGFmdGVyd2FyZHMuIE5vdGU6IEl0IGlzIHBvc3NpYmxlIHRvIGhhdmUgeW91ciBweXRob24KICBpbnN0YWxsZWQgaW4geW91ciB1c2VyJ3MgcmVhbG0gd2l0aG91dCB0aGUgbmVlZCBmb3IgYWRtaW5pc3RyYXRvcgogIHByaXZpbGVnZXMuCgogIEluIGEgY29tbWFuZGxpbmUgb3IgdGVybWluYWwgd2hlcmUgeW91IGhhdmUgYWNjZXNzIHRvIGBweXRob24nIHlvdSBjYW4KICB0aGVuIHNpbXBseSBzdGFydCB0aGUgZGN4IGNsaSBieSBydW5uaW5nOgoKICAsLS0tLQogIHwgcHl0aG9uIC1tIGRjeAogIGAtLS0tCgogIG9yIHBlcmhhcHMgd2l0aCBtb3JlIHBhcmFtZXRlcnMgKHNpbWlsYXIgdG8gYC0taGVscCcpOgoKICAsLS0tLQogIHwgcHl0aG9uIC1tIGRjeCAtLWhlbHAKICBgLS0tLQoKCjEuMiBQT1NULUlOU1RBTExBVElPTgp+fn5+fn5+fn5+fn5+fn5+fn5+fn4KCiAgWW91IGhhdmUgKG9idmlvdXNseSkgbWFuYWdlZCB0byBpbnN0YWxsIGBkY3gnIGFscmVhZHkuIEdyZWF0IQoKICBJIHJlY29tbWVuZCBwdXR0aW5nIGEgc3RhcnRlciBiYXNoIHNjcmlwdCBzb21ld2hlcmUgaW4geW91ciBgUEFUSCcsIHNvCiAgeW91IGNhbiBqdXN0IHJ1biBgZGN4JyB3aXRob3V0IHRoZSBweXRob24gdmVudiBpbml0LgoKICBGb3IgZXhhbXBsZSwgeW91IGNvdWxkIGhhdmUgYSBgZGN4JyBmaWxlIGJlbmVhdGggYC91c3IvbG9jYWwvYmluLycKICAoY2hhbmdlIHlvdXIgdmVudiBwYXRoIGlmIG5lY2Vzc2FyeSk6CgogICwtLS0tCiAgfCAjIS9iaW4vYmFzaAogIHwgCiAgfCAuIH4vdmVudi9iaW4vYWN0aXZhdGUKICB8IHB5dGhvbiAtbSBkY3ggIiRAIgogIGAtLS0tCgoKMS4zIFdPUktGTE9XIERFRklOSVRJT04gRk9STUFUCn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+fgoKMS4zLjEgRElSRUNUT1JZIFNUUlVDVFVSRQotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgogIEEgd29ya2Zsb3cgY29uc2lzdHMgKGluIGl0cyBtb3N0IHNpbXBsZSBmb3JtKSBvZiBleGFjdGx5ICpvbmUgZmlsZSoKICBuYW1lZCBgcGxheS5qcycgaW4geW91ciB3b3JraW5nIGRpcmVjdG9yeS4KCgoxLjMuMiBGSUxFIEZPUk1BVAotLS0tLS0tLS0tLS0tLS0tLQoKICBgcGxheS5qcycgaXMgSlNPTiB3aXRoICpvbmx5KiBvbmUgcm9vdCBlbGVtZW50LCBhbiBhcnJheSBgW10nLgoKICBUaGlzIGFycmF5IHN0b3JlcyBhbGwgbGluZWFyIGV4ZWN1dGVkIGBwbGF5X3N0ZXBzJywgd2hpY2ggdGhlbXNlbHZlcwogIGFyZSBhcnJheXMsIGFnYWluLiBUaGV5IHdpbGwgbGF0ZXIgYmUgZXhlY3V0ZWQgaW4tb3JkZXIgZnJvbSB0b3AgdG8KICBib3R0b20uCgogIEJhc2ljIGBwbGF5LmpzJyBzdHJ1Y3R1cmFsIChzdGlsbCBubyBjb250ZW50KToKICAsLS0tLQogIHwgWwogIHwgICBbXSwKICB8ICAgW10sCiAgfCAgIFtdCiAgfCBdCiAgYC0tLS0KCiAgVGhlc2UgKmlubmVyKiBhcnJheXMgKHRoZSBgcGxheV9zdGVwcycpIEFMV0FZUyBjb25zaXN0IG9mIGF0IGxlYXN0IDIKICBjb2x1bW5zLgoKICAxc3QgY29sdW1uOiBgIkpTT04gZW5jb2RlZCBYUGF0aCBTdHJpbmciIHwgbnVsbCcKCiAgMm5kIGNvbHVtbjogYENPTU1BTkQnIG5hbWUsIGFzIFN0cmluZwoKICAzcmQsIDR0aCwgLi4uIGNvbHVtbjogKE9wdGlvbmFsKSBwb3NpdGlvbmFsIHBhcmFtZXRlcnMgZm9yIHRoZSB1c2VkCiAgYENPTU1BTkQnLgoKICBOb3RlOiBBbGwgY29sdW1ucyAqaGF2ZSB0byBiZSogSlNPTiBTdHJpbmdzICh3aXRoIHRoZSBleGNlcHRpb24gb2YgdGhlCiAgMXN0LCB3aGljaCBjYW4gYmUgSlNPTjpudWxsIGluIGNhc2Ugb2YgYSBgQ09NTUFORCcgdGhhdCBkb2VzIG5vdAogIHJlbGF0ZSB0byBhbnkgd2Vic2l0ZS1lbGVtZW50KS4KCgoxLjMuMyBNSU5JTUFMIEVYQU1QTEUgYHBsYXkuanMnCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiAgVGhpcyBleGFtcGxlIG1heSBnaXZlIHlvdSBhIGJldHRlciBpZGVhOgoKICBgcGxheS5qcyc6CiAgLC0tLS0KICB8IFsKICB8ICAgW251bGwsICJnZXQiLCAiaHR0cHM6Ly8xMjcuMC4wLjE6ODA4MC8iXSwKICB8ICAgW251bGwsICJoYWx0Il0KICB8IF0KICBgLS0tLQoKICBXaGF0IHlvdSBzZWUgaXMgYW4gZXhhbXBsZSBwbGF5IHdpdGggb25seSAyIGNvbW1hbmQgaW52b2NhdGlvbnMuCgogIFRoZSAxc3QgY29tbWFuZCBpcyBgZ2V0Jywgd2hpY2ggZXF1YWxzIHRvIHR5cGluZyB0aGUgZm9sbG93aW5nIFVSTAogIGludG8geW91ciBhZGRyZXNzIGJhciBhbmQgb3BlbmluZyBpdC4KCiAgVGhlIDJuZCBjb21tYW5kIGtlZXBzIHRoZSBicm93c2VyIG9wZW4gYW5kIHlvdXIgY29tbWFuZGxpbmUgZ29pbmcgaW50bwogIGtpbmQgb2YgYW4gKmludGVyYWN0aXZlKiBtb2RlLiBXaXRob3V0IHRoZSBgaGFsdCcgY29tbWFuZCwgeW91cgogIGJyb3dzZXIgd291bGQgaW1tZWRpYXRlbHkgY2xvc2UgYW5kIGRpc2FwcGVhciBhZnRlciBvcGVuaW5nIHRoZSBVUkwKICBmcm9tIHRoZSBwcmV2aW91cyBzdGVwLiBUbyBza2lwIG91dCB0aGUgaW50ZXJhY3RpdmUgcHJvbXB0LCBqdXN0IHByZXNzCiAgUkVUVVJOLgoKCjEuNCBDUkVBVEUgTkVXIFdPUktGTE9XCn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+CgogIENyZWF0aW5nIGEgbmV3IHdvcmtmbG93L3Rlc3QvcGxheSAod2hhdGV2ZXIgeW91IHdhbnQgdG8gY2FsbCBpdCkKICBzaG91bGQgYWx3YXlzIGhhcHBlbiBpbiBhIG5ldyBlbXB0eSBkaXJlY3RvcnkuCgogIFRvIG1ha2UgaXQgYSBsaXR0bGUgZWFzaWVyIHRvIHN0YXJ0LCB5b3UgY2FuIHJ1bgoKICAsLS0tLQogIHwgbWtkaXIgRVhBTVBMRV9XT1JLRkxPVwogIHwgY2QgRVhBTVBMRV9XT1JLRkxPVwogIHwgZGN4IC0tZ2VuCiAgYC0tLS0KCiAgdG8gY3JlYXRlIGEgc2ltcGxlIHNhbXBsZSBgcGxheS5qcycgZmlsZSBpbiB5b3VyIG5ldyB3b3JraW5nIGRpcmVjdG9yeQogIChoZXJlOiBgRVhBTVBMRV9XT1JLRkxPVycpLgoKCjEuNSBSVU4gVEhFIE5FVyBXT1JLRkxPVwp+fn5+fn5+fn5+fn5+fn5+fn5+fn5+fn4KCiAgQmVmb3JlIHlvdSBzdGFydCwgeW91IG5lZWQgdG8ga25vdyB3aGljaCBicm93c2VyIHRvIHVzZS4gSW52b2tpbmcganVzdAogIHBsYWluIGBkY3gnIHdpbGwgdHJ5IGZpcmVmb3guIFlvdSBjYW4gb3ZlcnJpZGUgdGhpcyBiZWhhdmlvdXIgYnkKICBhZGRpbmcgYC0tbG9jYWwtY2hyb21lJyB0byB1c2UgY2hyb21lIGluc3RlYWQuCgogICwtLS0tCiAgfCBjZCBFWEFNUExFX1dPUktGTE9XCiAgfCBkY3ggICAgICAgICAgICAgICAgICAgICMgZm9yIGZpcmVmb3gKICB8IGRjeCAtLWxvY2FsLWNocm9tZSAgICAgIyBmb3IgY2hyb21lCiAgYC0tLS0KCiAgTm90ZTogVGhlIGRpcmVjdG9yeSBgbG9nJyB3aWxsIGJlIGNyZWF0ZWQgZHVyaW5nIHJ1bnRpbWUgLSBhbmQgZGVsZXRlZAogIGF1dG9tYXRpY2FsbHkuIElGIFlPVSBXQU5UIFRPIEtFRVAgSVQgRk9SIElOU1BFQ1RJT04sIEFERCBgLS1sb2cnLgoKCjEuNiBESVJFQ1RPUlkgYGxvZycgQUZURVIgRVhFQ1VUSU9OCn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+fn5+CgogIFdBUk5JTkc6IEJ5LWRlZmF1bHQgdGhlIGBsb2cnIGRpcmVjdG9yeSB3aWxsIGFsd2F5cyBiZSByZW1vdmVkCiAgKHJlY3Vyc2l2ZSwgbm8tcHJvbXB0KS4KCgoyIENPTU1BTkQgUkVGRVJFTkNFCj09PT09PT09PT09PT09PT09PT0KCjIuMSBPVkVSVklFVwp+fn5+fn5+fn5+fn4KCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIENvbW1hbmQgICAgICAgICAgICAgRGVzY3JpcHRpb24gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgRXhhbXBsZSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBhdHRyaWJ1dGVfc2V0ZW52JyAgQWRkIHNwZWNpZmllZCBlbGVtZW50J3MgYXR0cmlidXRlIHRvIEVOViAgICAgICAgICAgICAgICAgYFsiaWQ6YnV0dG9uOSIsICJhdHRyaWJ1dGVfc2V0ZW52IiwgImNsYXNzIiwgIkJVVFRPTjlfQ1NTX0NMQVNTRVMiXScgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBiYXNoJyAgICAgICAgICAgICAgRXhlY3V0ZSBhIGJhc2ggY29tbWFuZCB3aXRob3V0IHNpbmdsZSB0aWNzICAgICAgICAgICAgICAgYFtudWxsLCAiYmFzaCIsICJ1cHRpbWUgPiBhaGEiXScgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBiYXNoMCcgICAgICAgICAgICAgRXhlY3V0ZSBhIGJhc2ggY29tbWFuZCB3aXRob3V0IHNpbmdsZSB0aWNzIGFuZCByZXR1cm4gMCAgYFtudWxsLCAiYmFzaCIsICJlY2hvIG9rOyBleGl0IDEiXScgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBjbGVhcicgICAgICAgICAgICAgRW1wdHkgYDxJTlBVVD4nIG9yIGA8VEVYVEFSRUE+JyAgICAgICAgICAgICAgICAgICAgICAgICAgYFsiaWQ6Zmlyc3RuYW1lIiwgImNsZWFyIl0nICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBjbGljaycgICAgICAgICAgICAgQ2xpY2sgb24gZWxlbWVudCBDRU5URVIgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYFsiaWQ6YnRuLXN1Ym1pdCIsICJjbGljayJdJyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBnZXQnICAgICAgICAgICAgICAgT3BlbiBhIFVSTCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYFtudWxsLCAiZ2V0IiwgImh0dHBzOi8vd3d3Lmdvb2dsZS5kZSJdJyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBoYWx0JyAgICAgICAgICAgICAgRW50ZXIgYnJlYWtwb2ludCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYFtudWxsLCAiaGFsdCJdJyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBwYXRoJyAgICAgICAgICAgICAgT3BlbiBhIFBBVEgvVVJMIHZvbiB0aGUgc2FtZSBzZXJ2ZXIvaG9zdCAgICAgICAgICAgICAgICAgYFtudWxsLCAicGF0aCIsICIvaW5mby5odG1sIl0nICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBzYW0nICAgICAgICAgICAgICAgVXNlIGBzYXkgLXYgU2FtYW50aGEgPC4uLj4nIHRvIHNwZWFrIG9uIG1hY29zICAgICAgICAgICAgYFtudWxsLCAic2FtIiwgImFsbCBzeXN0ZW0gbm9taW5hbCJdJyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBzZXRlbnYnICAgICAgICAgICAgQWRkIG9yIGNoYW5nZSBFTlYgcGFyYW1ldGVycyBkdXJpbmcgcnVudGltZSAgICAgICAgICAgICAgYFtudWxsLCAic2V0ZW52IiwgIlBBUkFNX1giLCAiMTIzNCJdJyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBzZXR2YWx1ZScgICAgICAgICAgU2V0IGZvcm0gdmFsdWVzIHZpYSBqYXZhc2NyaXB0IGFuZCBub3Qgc2VuZGluZyBrZXlzICAgICAgYFsiaWQ6aW5wdXRmaWVsZDgiLCAic2V0dmFsdWUiLCAiSm9obiBEb2UiXScgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGBzbGVlcCcgICAgICAgICAgICAgRnJlZXplIEV4ZWN1dGlvbiBmb3IgU3BlY2lmaWVkIFNlY29uZHMgICAgICAgICAgICAgICAgICAgYFtudWxsLCAic2xlZXAiLCAiOCJdJyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCiAgIGB0eXBlJyAgICAgICAgICAgICAgU2VuZCBrZXlzIHRvIGVsZW1lbnQgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYFsiaWQ6ZnVua3lmaWVsZCIsICJ0eXBlIiwgIkhlbGxvIl0nICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCg=="
const_appversion = "0.42.0"


import base64
import os
import sys
import os.path
import logging
import json
import time
import traceback
import subprocess
import datetime
import argparse
import shutil

const_figlet = "IF9fXyAgIF9fX19fICBfXwp8ICAgXCAvIF9fXCBcLyAvCnwgfCkgfCAoX18gPiAgPCAKfF9fXy8gXF9fXy9fL1xfXAogICAgICAgICAgICAgICAgCg=="

import rich
from rich.console import Console

from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as CHOptions
from selenium.webdriver.edge.options import Options as EDOptions
from selenium import webdriver

from selenium.webdriver.common.keys import Keys as KEYS
from selenium.webdriver.common.by import By as BY

from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support.ui import Select as SEL
from selenium.webdriver.support import expected_conditions as EC

from urllib.parse import urlparse

import selenium
#from selenium.webdriver.firefox.firefox_profile import FirefoxProfile as FFProfile



epilog = base64.b64decode(const_epilog).decode()
figlet = base64.b64decode(const_figlet).decode()
parser = argparse.ArgumentParser(prog="dcx", epilog=epilog, formatter_class=argparse.RawTextHelpFormatter, description="DAISY CHAINED XPATH processor (v%s) - commandline tool to run JSON defined selenium scripts.\n\n%s\n" % (const_appversion, figlet))
parser.add_argument("--gen", action="store_true", help="Generate a play.js and play.env if non existing and QUIT")
parser.add_argument("--no-dev", action="store_true", help="Disable Developer Tools Auto-Open (Only Firefox)")
parser.add_argument("--log", action="store_true", help="Don't flush directory 'log'")
parser.add_argument("--local-chrome", action="store_true", help="Use local 'Google Chrome' and not 'Firefox'")
parser.add_argument("--ssl", action="store_true", help="Enforce valid SSL certificates (default without is ignoring SSL warnings, self-signed, ...)")
parser.add_argument("--debug", action="store_true", help="If an error occurs 'go interactive' and keep the window instead of shutting down")
parser.add_argument("--trace", action="store_true", help="If an error occurs also show a ASCII/src traceback")
parser.add_argument("--force", action="store_true", help="Use with caution (for --gen)")
parser.add_argument("--version", action="store_true", help="Show version and exit (no play.js running)")
parser.add_argument("--update", action="store_true", help="Compare with PyPI version and exit (no play.js running)")

args = parser.parse_args()


if args.version:
    print("dcx-%s(%s)" % (const_appversion, sys.platform))
    sys.exit(0)

if args.update:
    print("Looking up version on pypi.org, ...")
    import requests
    online_version = requests.get('https://pypi.org/pypi/dcx/json').json()["info"]["version"]
    recommend_txt = "nothing to do"
    if online_version != const_appversion:
        recommend_txt = "update to the latest version!"
    print("Latest=%s, installed=%s, %s" % (online_version, const_appversion, recommend_txt))
    sys.exit(0)


CONSOLE = Console()

FORMAT = '%(asctime)s+00:00 %(levelname)10s: %(message)-80s    (%(filename)s,%(funcName)s:%(lineno)s)'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.Formatter.converter = time.gmtime

# ==================================================================================== special case "gen"
if args.gen:
    if os.path.isfile("play.js") and args.force == False:
        logging.info("Won't overwrite play.js")
        sys.exit(1)
    else:
        with open('play.js', 'w') as f:
            f.write("""[
    ["//", "========================================================================================================="],
    ["//", "This is an example file - making it hopefully easier to start things for you when you're new to this!"],
    ["//", "========================================================================================================="],
    ["//", "- A play.js file is valid JSON and consists of ONLY ONE singular array (as you can see) with many, many STEPS being arrays for themselves - again"],
    ["//", "- All columns in a STEP array are typed as string! So don't put numbers or booleans in it! (ok, first column can be real null)"],
    ["//", "- If a STEP's first column is a double slash '//' it won't be executed. Just make sure it's still JSON..."],
    ["//", "- 1st column of a step refers to an element with a XPath expression (beware of the escaping, JSON, ...)"],
    ["//", "- 2st column is the actual command you want to execute - followed by any needed columns for parameters"],
    ["//", "- Don't forget - last command must not have a trailing comma, this is JSON..."],
    ["//", "- Your default ENV is prefilled 2 variables: $PWD, $HOME . They can directly be used in 'env' expansion for inputs, ..."],
    ["//", "- Extend four ENV by creating a play.env file. Don't use any ticks after the '=' sign"],
    ["//", ""],
    
    [null, "get", "https://google.de"],
    [null, "path", "/why"],

    [null, "halt"]                    
]
""")
        logging.info("play.js written successfully, terminating")
        sys.exit(0)
# ==================================================================================== special case "gen" end

default_wait = 30
opts = FFOptions()

if args.no_dev == False:
    opts.add_argument("-devtools")

opts.set_preference('media.mediasource.enabled', False)
if args.ssl:
    opts.accept_insecure_certs = False
else:
    opts.accept_insecure_certs = True

#opts = EDOptions()
#opts = CHOptions()

#driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=opts)

driver_mode = "local-firefox"
driver = None
if args.local_chrome:
    driver_mode = "local-chrome"
    chrome_options = CHOptions()
    if args.ssl == False:
        chrome_options.add_argument('ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
else:
    driver = webdriver.Firefox(options=opts)


logbasedir = os.path.join("log", driver_mode, sys.platform.lower() + "-" + datetime.datetime.today().strftime("%Y-%m-%d-%H%M%S"))
os.makedirs(logbasedir, exist_ok=False)

logdir_reg = os.path.join(logbasedir, "reg")
os.makedirs(logdir_reg, exist_ok=False)

logdir_viewport_img = os.path.join(logbasedir, "viewport-img")
os.makedirs(logdir_viewport_img, exist_ok=False)

logdir_full_img = os.path.join(logbasedir, "full-img")
os.makedirs(logdir_full_img, exist_ok=False)


reg_activity_log = {}

def reg_write(k, v):
    if not k in reg_activity_log.keys():
        reg_activity_log[k] = len(reg_activity_log.keys())
    with open(os.path.join(logdir_reg, k), 'w') as f:
        f.write(v)

def reg_read(k):
    with open(os.path.join(logdir_reg, k), 'r') as f:
        return f.read()

def content_provider_facade(src, provider_name=""):
    if "+" in provider_name:
        provider_chain = provider_name.split("+")
        for ci in provider_chain:
            src = content_provider_facade(src, ci)
        return src
    if provider_name == "":
        return src
    if provider_name == "bash":
        return subprocess.check_output("""/bin/bash -c '%s'""" % src, shell=True, universal_newlines=True)
    if provider_name == "env":
        for k in envdata.keys():
            kstring = "$" + k
            src = src.replace(kstring, envdata[k])
        return src


def get_all_a_href(min_slashes=0, beneath=None):
    all_href={}
    all_a = driver.find_elements(BY.XPATH, "//a")
    if beneath is not None:
        all_a = beneath.find_elements(BY.XPATH, ".//a")
    for a in all_a:
        href = a.get_attribute("href")
        ac = ['_' for x in href if x=="/"]
        if len(ac) >= min_slashes:
            all_href[href] = True
    return sorted(list(all_href.keys()))


def break_handler(data):
    if data == "?":
        print("")
        print("HELP")
        print("")
    if data == "d":
        b = driver.find_element(BY.XPATH, "//body")
        with open("BODY", "w") as bf:
            bf.write(b.get_attribute("innerHTML"))

        # with open("A", "w") as af:
        #     af.write("\n".join(get_all_a_href(5)))


        pass
        #debug dev
        # vids = driver.find_elements(BY.XPATH, "//video/source")
        # for v in vids:
        #     print(v)
        #     print("_%s_" % v.get_attribute("src"))
        #     print("===")
    if data == "h":
        print("href=%s" % driver.execute_script('return location.href;'))
    if data == "r":
        print("Dumping registry: %d entries" % len(reg_activity_log))
        for x in reg_activity_log.keys():
            print("  %s = %s" % (x, reg_read(x)))
    if data == "q":
        print("QUIT")
        driver.quit()
        if args.log == False:
            shutil.rmtree(logbasedir)
        sys.exit(0)

# src=["b", "n"], l=2, idx=1
def expand_column(src, idx):
    content = src[idx]
    if idx+1 <= len(src)-1:
        content = content_provider_facade(content, src[idx+1])
    return content


envdata = {}
envdata["HOME"] = os.getenv("HOME")
envdata["PWD"] = os.getenv("PWD")


def interactive_break():
    while True:
        print("*** DEBUG HALT ***")
        break_input = input("Press RETURN (no input) to continue (leave DEBUG HALT)... $ ")
        if break_input == "":
            break
        else:
            break_handler(break_input)



if os.path.isfile("play.js"):

    if os.path.isfile("play.env"):
        envlines = [l.strip() for l in open("play.env", "r").read().strip().split() if l.strip() != ""]
        for l in envlines:
            epos=l.find("=")
            k = l[0:epos]
            v = l[epos+1:]
            envdata[k]=v

    logging.info("env is " + str(envdata))


    play = json.loads(open("play.js", "r").read())
    play_part_i = 0
    for play_part in play:
        ppl = len(play_part) # play part length
        play_part_i+=1

        try:

            logdir_part = os.path.join(logbasedir, "parts", "part-%04d" % play_part_i)
            os.makedirs(logdir_part, exist_ok=False)

            #pre tasks
            viewport_png_in = os.path.join(logdir_viewport_img, 'part-%08d-in.png' % play_part_i)
            driver.save_screenshot(viewport_png_in)

            if callable(hasattr(driver, 'save_full_page_screenshot')): # only firefox has it
                full_png_in = os.path.join(logdir_full_img, 'part-%08d-in.png' % play_part_i)
                driver.save_full_page_screenshot(full_png_in)

            unknown_command = True
            if play_part[0] == None:
                
                if play_part[1] == "bash": ###ntcommand
                    bash_command = expand_column(play_part, 2)
                    logging.info("Will execute bash with '%s'" % bash_command)
                    bash_o = subprocess.check_output("""/bin/bash -c '%s'""" % bash_command, shell=True, universal_newlines=True)
                    unknown_command=False

                if play_part[1] == "bash0": ###ntcommand
                    bash_command = expand_column(play_part, 2)
                    logging.info("Will execute bash with '%s'" % bash_command)
                    bash_o = subprocess.check_output("""/bin/bash -c '%s; exit 0'""" % bash_command, shell=True, universal_newlines=True)
                    unknown_command=False

                if play_part[1] == "conf": ###ntcommand
                    conf_k = play_part[2]
                    conf_v = play_part[3]
                    conf_ok = False
                    
                    if conf_k == "default_wait":
                        default_wait = int(conf_v)
                        logging.info("reconfig: default_wait set to %d seconds" % default_wait)
                        conf_ok=True
                        unknown_command=False
                    
                    if conf_ok == False:
                        raise Exception("Unable to reconfigure with - %s" % str(play_part))

                if play_part[1] == "get": ###ntcommand
                    url_for_get = expand_column(play_part, 2)
                    driver.get(url_for_get)
                    unknown_command=False

                if play_part[1] == "setenv": ###ntcommand
                    env_key = play_part[2]
                    env_value = expand_column(play_part, 3)
                    envdata[env_key] = env_value
                    unknown_command=False

                if play_part[1] == "sam": ###ntcommand
                    sentence = play_part[2]
                    subprocess.call("""/bin/bash -c "say -v Samantha '%s'; exit 0" """ % sentence, shell=True)
                    unknown_command=False

                if play_part[1] == "max": ###ntcommand
                    driver.maximize_window()
                    time.sleep(1)
                    unknown_command=False

                if play_part[1] == "window": ###ntcommand
                    window_spec = play_part[2]
                    if window_spec == "max":
                        driver.maximize_window()
                        unknown_command=False
                    if window_spec == "vga":
                        driver.set_window_size(640, 480)
                        unknown_command=False
                    if window_spec == "svga":
                        driver.set_window_size(800, 600)
                        unknown_command=False
                    if window_spec == "xga":
                        driver.set_window_size(1024, 768)
                        unknown_command=False
                    if window_spec == "sxga":
                        driver.set_window_size(1280, 1024)
                        unknown_command=False
                    if window_spec == "wuxga":
                        driver.set_window_size(1920, 1200)
                        unknown_command=False
                    if window_spec == "iphone12":
                        driver.set_window_size(390, 844)
                        unknown_command=False
                    time.sleep(1)

                if play_part[1] == "path": ###ntcommand
                    urlpart_for_get = expand_column(play_part, 2)
                    url_actual = driver.execute_script('return location.href;').strip().split("\n")[0].strip()
                    url_data = urlparse(url_actual)
                    url_target = url_data.scheme + "://" + url_data.netloc + urlpart_for_get
                    driver.get(url_target)
                    unknown_command=False

                if play_part[1] == "sleep":###ntcommand
                    if ppl == 2:
                        time.sleep(1)
                    else:
                        time.sleep(float(play_part[2]))
                    unknown_command=False

                if play_part[1] == "halt":###ntcommand
                    interactive_break()
                    unknown_command=False

                if play_part[1] == "click_any_const":###ntcommand
                    any_consts = [x for x in play_part[2:]]
                    constructed_xpath = "//*[" + " or ".join(["text()=\"%s\"" % x for x in any_consts]) + "]"
                    any_lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.XPATH, constructed_xpath))
                    if any_lel is None or len(any_lel) == 0:
                        raise Exception("could not click one of %s" % str(any_consts))
                    #driver.execute_script("arguments[0].scrollIntoView(true);", any_lel[0])
                    any_lel[0].click()
                    unknown_command=False

                if play_part[1] == "click_any_const_contains":###ntcommand
                    any_consts = [x for x in play_part[2:]]
                    constructed_xpath = "//*[" + " or ".join(["contains(., \"%s\")" % x for x in any_consts]) + "]"
                    any_lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.XPATH, constructed_xpath))
                    if any_lel is None or len(any_lel) == 0:
                        raise Exception("could not click one of %s" % str(any_consts))
                    #driver.execute_script("arguments[0].scrollIntoView(true);", any_lel[0])
                    any_lel[0].click()
                    unknown_command=False

                if play_part[1] == "click_any_const_startswith":###ntcommand
                    any_consts = [x for x in play_part[2:]]
                    constructed_xpath = "//*[" + " or ".join(["starts-with(., \"%s\")" % x for x in any_consts]) + "]"
                    logging.info(constructed_xpath)
                    any_lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.XPATH, constructed_xpath))
                    if any_lel is None or len(any_lel) == 0:
                        raise Exception("could not click one of %s" % str(any_consts))
                    any_lel[0].click()
                    unknown_command=False

                if play_part[1] == "js64str":###ntcommand
                    varname = play_part[2]
                    code_plain = base64.b64decode(play_part[3]).decode("utf-8")
                    res = str(driver.execute_script(code_plain))
                    reg_write(varname, res)
                    unknown_command=False

                # if play_part[1] == "a":###ntcommand
                #     varname = play_part[2]
                #     res="\n".join(get_all_a_href())
                #     reg_write(varname, res)
                #     unknown_command=False


            else:
                lel = None # list of elements
                
                if play_part[0] == "//":
                    unknown_command=False
                else:

                    if play_part[0].startswith("id:"):
                        target_id = play_part[0][3:]
                        lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.ID, target_id))
                    else:
                        lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.XPATH, play_part[0]))

                    # if play_part[1] == "a":###tcommand
                    #     varname = play_part[2]
                    #     res="\n".join(get_all_a_href(beneath=lel[0]))
                    #     reg_write(varname, res)
                    #     unknown_command=False

                    if play_part[1] == "reg_dom":###tcommand
                        varname = play_part[2]
                        reg_write(varname, lel[0].get_attribute("innerHTML"))
                        unknown_command=False

                    if play_part[1] == "attribute_setenv":###tcommand
                        attribute_name = play_part[2]
                        env_key = play_part[3]
                        envdata[env_key] = lel[0].get_attribute(attribute_name)
                        unknown_command=False

                    if play_part[1] == "reg_dom1":###tcommand
                        varname = play_part[2]
                        reg_write(varname, lel[0].get_attribute("innerHTML").replace("><", ">\n<"))
                        unknown_command=False

                    if play_part[1] == "reg_attr":###tcommand
                        attrname = play_part[2]
                        varname = play_part[3]
                        res=str(lel[0].get_attribute(attrname))
                        reg_write(varname, res)
                        unknown_command=False

                    if play_part[1] == "siv":###tcommand
                        driver.execute_script("arguments[0].scrollIntoView(true);", lel[0])
                        time.sleep(1);
                        unknown_command=False

                    if play_part[1] == "type": ###tcommand
                        content = expand_column(play_part, 2)
                        # content = play_part[2]
                        # if ppl > 3:
                        #     content = content_provider_facade(content, play_part[3])
                        if driver_mode.upper().find("CHROME") >= 0:
                            logging.warn("You are using send_keys (dcx:type) for chrome which may lead to unwanted form submits - consider dcx:setvalue instead.")
                        lel[0].send_keys(content)
                        unknown_command=False

                    # kind of "clear and silent type"
                    if play_part[1] == "setvalue": ###tcommand
                        content = expand_column(play_part, 2)
                        # content = play_part[2]
                        # if ppl > 3:
                        #     content = content_provider_facade(content, play_part[3])
                        #lel[0].send_keys(content)
                        driver.execute_script("arguments[0].value = arguments[1];", lel[0], content)
                        unknown_command=False

                    if play_part[1] == "click": ###tcommand
                        lel[0].click()
                        unknown_command=False

                    if play_part[1] == "checked": ###tcommand
                        if lel[0].is_selected() == False:
                            lel[0].click()
                        unknown_command=False

                    if play_part[1] == "checkedjs": ###tcommand
                        driver.execute_script("arguments[0].checked = true;", lel[0])
                        unknown_command=False

                    if play_part[1] == "uncheckedjs": ###tcommand
                        driver.execute_script("arguments[0].checked = false;", lel[0])
                        unknown_command=False

                    if play_part[1] == "unchecked": ###tcommand
                        if lel[0].is_selected() == True:
                            lel[0].click()
                        unknown_command=False

                    if play_part[1] == "clickif": ###tcommand
                        e_type = play_part[2]
                        e_contains = play_part[3]
                        constructed_xpath = "//%s[contains(., \"%s\")]" % (e_type, e_contains)
                        sub_lel = lel[0].find_elements(BY.XPATH, constructed_xpath)
                        if sub_lel is None or len(sub_lel) == 0:
                            logging.info("clickif empty")
                        else:
                            sub_lel[0].click()
                        #any_lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.XPATH, constructed_xpath))
                        unknown_command=False


                    if play_part[1] == "checked01": ###tcommand
                        varname = play_part[2]
                        if lel[0].is_selected():
                            reg_write(varname, '1')
                        else:
                            reg_write(varname, '0')
                        logging.info("REG: %s = %s" % (varname, reg_read(varname)))
                        unknown_command=False

                    if play_part[1] == "clear": ###tcommand
                        lel[0].clear()
                        unknown_command=False
            
            if unknown_command:
                raise Exception("Command '%s' is unknown" % play_part[1])

            #post tasks
            viewport_png_out = os.path.join(logdir_viewport_img, 'part-%08d-out.png' % play_part_i)
            driver.save_screenshot(viewport_png_out)

            if callable(hasattr(driver, 'save_full_page_screenshot')): # only firefox has it
                full_png_out = os.path.join(logdir_full_img, 'part-%08d-out.png' % play_part_i)
                driver.save_full_page_screenshot(full_png_out)

        except Exception as exc:
            logging.error(exc)

            if args.trace:
                CONSOLE.print_exception()
            if args.debug:
                interactive_break()
            break

# end of for in parts...

# driver.save_screenshot("test.png")
driver.quit()
logging.info("finished")

if args.log == False:
    shutil.rmtree(logbasedir)
