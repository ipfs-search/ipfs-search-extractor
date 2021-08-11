# ipfs-search-extractor
Extract data from ipfs-search' database, for phun and profit.

## Requirements
- Python 3
- pipenv

## Usage
1. `pipenv shell`
2. `python extractor.py`
3. Behold result.
4. Tweak parameters (in script).

## Example
### 2018
```bash
(ipfs-search-extractor) $ python extractor.py | bzip2 -c > exports/ipfs-search-2018.json.bz2
131645 documents written in 57.59049701690674
First item: 2018-01-16T18:46:00Z
Last item: 2018-12-31T23:58:57Z
```

## Example output
```json
[
  "QmbAvZoiPvAaLY6vFyQSxAaMhzSa5vp2CDi4LzRejpw9DZ",
  "xkcd: Brontosaurus",
  "2018-01-16T18:46:00Z"
],
[
  "QmcZ2a1tQpDUoDFGHhXs6Ga795LAbX2t4FEuTBYWxLYuUP",
  "Botany Readings",
  "2018-01-16T18:46:15Z"
],
...
```

## Field description
For efficiency reasons, we are omitting field names. We're using JSON mainly to avoid encoding issues.
```json
[
  "<CID>",
  "<title>",
  "<first-seen>"
]
```

## Example exports (links on IPFS)
- [2018](https://gateway.ipfs.io/ipfs/Qmb2JizJSE5HCmzP6qKiRPmamGdgV6Aes2UudzYrgphfvC) (5.97 MiB)
- [2019](https://gateway.ipfs.io/ipfs/QmZgP278dJHA5RZgsD1kVQM2Jzmo5sN8Z7Aoj179j3G49c) (10.24 MiB, 131645 documents)
- [2020](https://gateway.ipfs.io/ipfs/QmZcMDBpAso15QqaGeG4jtiKavXmQkFBEPhGHxNGkD9qcN) (20.12 MiB, 450436 documents)
- [2021, until 10-8](https://gateway.ipfs.io/ipfs/QmP8E1rio395xfZDk4SWRygC3P13Jfyy1ycDxoyEXRyNAA) (456.52 MiB, 10485760 documents)
Note that the greater majority of files on ipfs-search.com seem not to have an extracted title!

