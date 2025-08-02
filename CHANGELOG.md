# Changelog

## 2.9.0 (2025-08-02)

Full Changelog: [v2.8.0...v2.9.0](https://github.com/evrimai/python-client/compare/v2.8.0...v2.9.0)

### Features

* **api:** api update ([#71](https://github.com/evrimai/python-client/issues/71)) ([f1d74e2](https://github.com/evrimai/python-client/commit/f1d74e2bd52f9c00e8d14c894716b2719469b260))


### Bug Fixes

* **package:** support direct resource imports ([db3beee](https://github.com/evrimai/python-client/commit/db3beee83baa64b866436c219e6f7d8c5df1a136))
* **perf:** optimize some hot paths ([2130460](https://github.com/evrimai/python-client/commit/21304602461229683e8e63f72e0122550b05a618))
* **perf:** skip traversing types for NotGiven values ([62cf11f](https://github.com/evrimai/python-client/commit/62cf11fba968715c7b31d901c8f5f34a30c8fa3a))
* **pydantic v1:** more robust ModelField.annotation check ([c9e8911](https://github.com/evrimai/python-client/commit/c9e89114a21af9de22041087891f2b6cdea8dae9))


### Chores

* broadly detect json family of content-type headers ([893312b](https://github.com/evrimai/python-client/commit/893312b59fd147d1356c543ecef0195387d3aa26))
* **ci:** add timeout thresholds for CI jobs ([e3ab35a](https://github.com/evrimai/python-client/commit/e3ab35a64fd929598a179e0060020676d8021c29))
* **ci:** fix installation instructions ([1edfc67](https://github.com/evrimai/python-client/commit/1edfc678a53fc7ad6f86170a9dbbb606cde8baca))
* **ci:** only use depot for staging repos ([efaf732](https://github.com/evrimai/python-client/commit/efaf732c2b77ec26698b61dde3b9dc017cfc725b))
* **ci:** upload sdks to package manager ([6ee22ad](https://github.com/evrimai/python-client/commit/6ee22adb50be0070098473c84a7ac1d00a5a2bff))
* **client:** minor internal fixes ([024b925](https://github.com/evrimai/python-client/commit/024b9254751ef8643f0b72037b0e0d7f0f526798))
* **docs:** grammar improvements ([60b41d0](https://github.com/evrimai/python-client/commit/60b41d0be94a2e55a1cc126373f042bc9d4c5273))
* **internal:** avoid errors for isinstance checks on proxies ([b109cd3](https://github.com/evrimai/python-client/commit/b109cd3d1021ef045774eab4c9068810bd915227))
* **internal:** base client updates ([bd85924](https://github.com/evrimai/python-client/commit/bd85924eebfe9f9e6e0b205a83857cd6c3dbfd2b))
* **internal:** bump pyright version ([730f781](https://github.com/evrimai/python-client/commit/730f781a69dd8f10c9f5cc63c79b718541e51c4a))
* **internal:** codegen related update ([a5c88eb](https://github.com/evrimai/python-client/commit/a5c88ebfa9dc2918c163753e090ffe8afaf7d2df))
* **internal:** expand CI branch coverage ([064117a](https://github.com/evrimai/python-client/commit/064117a7bce50f9d30e416365d912fddd4a5318f))
* **internal:** fix list file params ([4ac36d0](https://github.com/evrimai/python-client/commit/4ac36d01d2bc29c158fd5f0a598dfb4dc7e48c12))
* **internal:** import reformatting ([0541854](https://github.com/evrimai/python-client/commit/05418549ab67acf639f7cd9300e3971262d3fa8b))
* **internal:** minor formatting changes ([0ef9e84](https://github.com/evrimai/python-client/commit/0ef9e84193f9b9ef3db29972d7981766fac89628))
* **internal:** reduce CI branch coverage ([e0381ae](https://github.com/evrimai/python-client/commit/e0381ae7b71c11737c073e30ec83a890e0ee147a))
* **internal:** refactor retries to not use recursion ([85d0556](https://github.com/evrimai/python-client/commit/85d0556f0a2eb3727941f0230f47ac1fb9869c9a))
* **internal:** remove trailing character ([#73](https://github.com/evrimai/python-client/issues/73)) ([75e43a9](https://github.com/evrimai/python-client/commit/75e43a9ab76587d240d151003f1f8a9d37a82ca2))
* **internal:** slight transform perf improvement ([#74](https://github.com/evrimai/python-client/issues/74)) ([9808a93](https://github.com/evrimai/python-client/commit/9808a9315129182b4304802653ce7b27ddd83ad7))
* **internal:** update models test ([02396c5](https://github.com/evrimai/python-client/commit/02396c5343fa736ec016cb541e803dbbd95792c0))
* **internal:** update pyright settings ([ccd70c6](https://github.com/evrimai/python-client/commit/ccd70c617998c7e2f0193455bd7b47b4da04e4e2))

## 2.8.0 (2025-03-27)

Full Changelog: [v2.7.0...v2.8.0](https://github.com/evrimai/python-client/compare/v2.7.0...v2.8.0)

### Features

* **api:** manual updates ([#68](https://github.com/evrimai/python-client/issues/68)) ([b8b211e](https://github.com/evrimai/python-client/commit/b8b211eaa628da7aa9053cb01b94dff404eee123))

## 2.7.0 (2025-03-27)

Full Changelog: [v2.6.1...v2.7.0](https://github.com/evrimai/python-client/compare/v2.6.1...v2.7.0)

### Features

* **api:** api update ([#64](https://github.com/evrimai/python-client/issues/64)) ([1627c45](https://github.com/evrimai/python-client/commit/1627c458e54a4b57d22ba4b83acaaf613cc9495f))
* **api:** api update ([#66](https://github.com/evrimai/python-client/issues/66)) ([20e909c](https://github.com/evrimai/python-client/commit/20e909c93400ad4a962d318b8850f52938a5611a))

## 2.6.1 (2025-03-20)

Full Changelog: [v2.6.0...v2.6.1](https://github.com/evrimai/python-client/compare/v2.6.0...v2.6.1)

### Features

* **api:** api update ([#62](https://github.com/evrimai/python-client/issues/62)) ([6a5576b](https://github.com/evrimai/python-client/commit/6a5576be1f5e6da46d1805ba0eb0f737c9443452))


### Bug Fixes

* **ci:** ensure pip is always available ([#60](https://github.com/evrimai/python-client/issues/60)) ([dfc58d4](https://github.com/evrimai/python-client/commit/dfc58d4473aad210b037e1ce320ff49aab4b6dd5))
* **ci:** remove publishing patch ([#61](https://github.com/evrimai/python-client/issues/61)) ([77c9b66](https://github.com/evrimai/python-client/commit/77c9b66e8bec6f294a6830027eb994a3bf2ef9d1))
* **types:** handle more discriminated union shapes ([#59](https://github.com/evrimai/python-client/issues/59)) ([9956f74](https://github.com/evrimai/python-client/commit/9956f744ea933e4b7887358a3aa53900d2fb4913))


### Chores

* **internal:** bump rye to 0.44.0 ([#58](https://github.com/evrimai/python-client/issues/58)) ([07dc6cb](https://github.com/evrimai/python-client/commit/07dc6cbe8eaf16c9ae47d588dda4dea1463aff85))
* **internal:** codegen related update ([#57](https://github.com/evrimai/python-client/issues/57)) ([7c49da5](https://github.com/evrimai/python-client/commit/7c49da5b3f4beaa6d0a69dcc3e75ce862d582ae5))
* **internal:** remove extra empty newlines ([#55](https://github.com/evrimai/python-client/issues/55)) ([2eec7ec](https://github.com/evrimai/python-client/commit/2eec7ecdc1093b5b56e2494731ed05c91b118ce2))

## 2.6.0 (2025-03-12)

Full Changelog: [v2.5.0...v2.6.0](https://github.com/evrimai/python-client/compare/v2.5.0...v2.6.0)

### Features

* **api:** api update ([#52](https://github.com/evrimai/python-client/issues/52)) ([73922e3](https://github.com/evrimai/python-client/commit/73922e302702b8e6402a758410a2628d5b12a1fa))

## 2.5.0 (2025-03-11)

Full Changelog: [v2.4.0...v2.5.0](https://github.com/evrimai/python-client/compare/v2.4.0...v2.5.0)

### Features

* **api:** api update ([#49](https://github.com/evrimai/python-client/issues/49)) ([84cb8c5](https://github.com/evrimai/python-client/commit/84cb8c5f9419efd9e6cbe5c31ebdf147957ed137))

## 2.4.0 (2025-03-11)

Full Changelog: [v2.3.0...v2.4.0](https://github.com/evrimai/python-client/compare/v2.3.0...v2.4.0)

### Features

* **api:** api update ([#47](https://github.com/evrimai/python-client/issues/47)) ([2407001](https://github.com/evrimai/python-client/commit/240700130f8a55325834c9742fc5cd8f02134819))


### Documentation

* revise readme docs about nested params ([#44](https://github.com/evrimai/python-client/issues/44)) ([c660316](https://github.com/evrimai/python-client/commit/c6603162721f87febb5d3decdcfb584299da120b))

## 2.3.0 (2025-03-04)

Full Changelog: [v2.2.1...v2.3.0](https://github.com/evrimai/python-client/compare/v2.2.1...v2.3.0)

### Features

* **api:** api update ([#35](https://github.com/evrimai/python-client/issues/35)) ([64dfb1f](https://github.com/evrimai/python-client/commit/64dfb1ff52376e845259ba48a028f4fba2d729a8))
* **client:** allow passing `NotGiven` for body ([#37](https://github.com/evrimai/python-client/issues/37)) ([9237c01](https://github.com/evrimai/python-client/commit/9237c0197cb4a55c8b23d5f418c53893ad7b1f3d))


### Bug Fixes

* **client:** mark some request bodies as optional ([9237c01](https://github.com/evrimai/python-client/commit/9237c0197cb4a55c8b23d5f418c53893ad7b1f3d))


### Chores

* **docs:** update client docstring ([#41](https://github.com/evrimai/python-client/issues/41)) ([cf42821](https://github.com/evrimai/python-client/commit/cf4282194d4f3690645e2e5b4237ed5efc440c69))
* **internal:** fix devcontainers setup ([#38](https://github.com/evrimai/python-client/issues/38)) ([32a10dc](https://github.com/evrimai/python-client/commit/32a10dc3ab18a7e9d74ab92707446b9dec4c847a))
* **internal:** properly set __pydantic_private__ ([#39](https://github.com/evrimai/python-client/issues/39)) ([762f1e2](https://github.com/evrimai/python-client/commit/762f1e26e38bd452043a7e35a3313e467e6c9e5b))
* **internal:** remove unused http client options forwarding ([#42](https://github.com/evrimai/python-client/issues/42)) ([f83be05](https://github.com/evrimai/python-client/commit/f83be0532ea982e95741d05633d11307332bc985))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#40](https://github.com/evrimai/python-client/issues/40)) ([a11c9a7](https://github.com/evrimai/python-client/commit/a11c9a7b194c26e350b74f375ae7504795a078a5))

## 2.2.1 (2025-02-14)

Full Changelog: [v2.2.0...v2.2.1](https://github.com/evrimai/python-client/compare/v2.2.0...v2.2.1)

### Bug Fixes

* asyncify on non-asyncio runtimes ([#33](https://github.com/evrimai/python-client/issues/33)) ([0f678a0](https://github.com/evrimai/python-client/commit/0f678a04c97b4f8b20cc0ff16e913df13271d468))


### Chores

* **internal:** update client tests ([#31](https://github.com/evrimai/python-client/issues/31)) ([662aa3f](https://github.com/evrimai/python-client/commit/662aa3fe8b98abb811f323efb6e08d8c039c93d7))

## 2.2.0 (2025-02-12)

Full Changelog: [v2.1.1...v2.2.0](https://github.com/evrimai/python-client/compare/v2.1.1...v2.2.0)

### Features

* **api:** api update ([#12](https://github.com/evrimai/python-client/issues/12)) ([24ef0a0](https://github.com/evrimai/python-client/commit/24ef0a091f8a0d459f3a530be720a05f69ae6001))
* **api:** api update ([#17](https://github.com/evrimai/python-client/issues/17)) ([c3ff323](https://github.com/evrimai/python-client/commit/c3ff3236d8668d1c99884fee1ab7f9fe727e1868))
* **api:** api update ([#22](https://github.com/evrimai/python-client/issues/22)) ([4113fd8](https://github.com/evrimai/python-client/commit/4113fd88272cb33c2145a705877ae9beddeeec25))
* **api:** api update ([#29](https://github.com/evrimai/python-client/issues/29)) ([f4f0571](https://github.com/evrimai/python-client/commit/f4f0571a214821dd6409ac7a876c64a99bdfe2db))
* **client:** send `X-Stainless-Read-Timeout` header ([#26](https://github.com/evrimai/python-client/issues/26)) ([8a40065](https://github.com/evrimai/python-client/commit/8a400654709e627ce4ef3d0d17a953f2bdc2e04b))


### Bug Fixes

* improve names for conflicting params ([#25](https://github.com/evrimai/python-client/issues/25)) ([edb909e](https://github.com/evrimai/python-client/commit/edb909e111568e81ac00d20a7c18f797e1a303bc))
* **tests:** correctly generate examples with writeOnly fields ([#21](https://github.com/evrimai/python-client/issues/21)) ([ff3dee5](https://github.com/evrimai/python-client/commit/ff3dee5c2e3a82a751437c52a0443bdedf6b9735))


### Chores

* **internal:** bummp ruff dependency ([#24](https://github.com/evrimai/python-client/issues/24)) ([2c9e3a7](https://github.com/evrimai/python-client/commit/2c9e3a73ecd12a00c33817917ecf6c9bddcfe32d))
* **internal:** change default timeout to an int ([#23](https://github.com/evrimai/python-client/issues/23)) ([739038c](https://github.com/evrimai/python-client/commit/739038cc61b63c6e4823d9ba3db3d0f4252f4d6d))
* **internal:** codegen related update ([#14](https://github.com/evrimai/python-client/issues/14)) ([f67fb19](https://github.com/evrimai/python-client/commit/f67fb1963737d3992fb655729fd9e2bad513a4e7))
* **internal:** codegen related update ([#15](https://github.com/evrimai/python-client/issues/15)) ([1c21cb4](https://github.com/evrimai/python-client/commit/1c21cb426aa089184cdd79bb5c1d949d8de39bae))
* **internal:** codegen related update ([#16](https://github.com/evrimai/python-client/issues/16)) ([bc5139d](https://github.com/evrimai/python-client/commit/bc5139da1e0ae996f9ee36d07735f739a400f4d5))
* **internal:** codegen related update ([#18](https://github.com/evrimai/python-client/issues/18)) ([8801a8d](https://github.com/evrimai/python-client/commit/8801a8d7bed8b234483b0c2144146467112fbb09))
* **internal:** codegen related update ([#19](https://github.com/evrimai/python-client/issues/19)) ([a733d12](https://github.com/evrimai/python-client/commit/a733d12fc61911da0e62d23c64cf3c638041cc6c))
* **internal:** fix type traversing dictionary params ([#27](https://github.com/evrimai/python-client/issues/27)) ([b351f2a](https://github.com/evrimai/python-client/commit/b351f2a7dd438677ab4426f82765dbcff09add0c))
* **internal:** minor formatting changes ([#20](https://github.com/evrimai/python-client/issues/20)) ([4d15cd0](https://github.com/evrimai/python-client/commit/4d15cd05b28a8d50b2897ddf770937f4e127fbb5))
* **internal:** minor type handling changes ([#28](https://github.com/evrimai/python-client/issues/28)) ([77c3e97](https://github.com/evrimai/python-client/commit/77c3e9716bc9373980e15b4f5993682b9f5cb813))

## 2.1.1 (2025-01-10)

Full Changelog: [v2.1.0...v2.1.1](https://github.com/evrimai/python-client/compare/v2.1.0...v2.1.1)

### Bug Fixes

* correctly handle deserialising `cls` fields ([#10](https://github.com/evrimai/python-client/issues/10)) ([022ce03](https://github.com/evrimai/python-client/commit/022ce03bbd753d947e8b0bb47216df124cfef0c7))


### Chores

* **internal:** version bump ([#8](https://github.com/evrimai/python-client/issues/8)) ([bc30d36](https://github.com/evrimai/python-client/commit/bc30d368e3a47f4516b0ee1ac5d6d5c9bf0d2747))

## 2.1.0 (2025-01-08)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/evrimai/python-client/compare/v2.0.0...v2.1.0)

### Features

* **api:** update via SDK Studio ([#5](https://github.com/evrimai/python-client/issues/5)) ([768b6fc](https://github.com/evrimai/python-client/commit/768b6fcc9838b5d84b879d0e53663e4f145e729b))
* **api:** update via SDK Studio ([#6](https://github.com/evrimai/python-client/issues/6)) ([27422a5](https://github.com/evrimai/python-client/commit/27422a5b19c7f634b0879f04e35651e6dfd40634))


### Chores

* **internal:** version bump ([#7](https://github.com/evrimai/python-client/issues/7)) ([1b24869](https://github.com/evrimai/python-client/commit/1b24869a016eb23bae79059ecb897297ca551201))
* update SDK settings ([#3](https://github.com/evrimai/python-client/issues/3)) ([3f60f18](https://github.com/evrimai/python-client/commit/3f60f18c14aeaab599a758244796417427b52897))

## 2.0.0 (2025-01-08)

Full Changelog: [v0.0.1-alpha.0...v2.0.0](https://github.com/evrimai/python-client/compare/v0.0.1-alpha.0...v2.0.0)

### Chores

* go live ([#1](https://github.com/evrimai/python-client/issues/1)) ([829c3fb](https://github.com/evrimai/python-client/commit/829c3fb6a9f59d38cea2d0f27893ad30ef1c7938))
