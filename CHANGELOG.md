# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - Current dev version - 0.0.11
### Added
### Fixed
### Changed
### Removed

## [0.0.10] - 2022-11-14
### Added
- CHANGELOG.md
- Hydrate object results from Sui `sui_executeTransaction` API (see sui/sui_tx_return_types.py)
- Transaction result tests (results are static via conftest.py fixtures in tests/unit)
- MovePackage dataclasses from API result
- Added requirements-dev.txt for local development
- DEVELOP.md for local development
- SDK version command in samples wallet
- `bin/` folder for utility functions
- `bin/publish.sh` for publishing `pysui` package to PyPi
- `-v,--version` command to `samples.wallet`
- `sphinx` in `requirements-dev.txt`
- `get_address_object_descriptors` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `get_objects_for` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `get_object` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `get_package` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `pay_txn` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `pay_sui_txn` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `pay_allsui_txn` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `transfer_sui_txn` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `transfer_object_txn` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `merge_coin_txn` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `split_coin_txn` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `move_call_txn` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)
- `publish_package_txn` on SuiClient [issue](https://github.com/FrankC01/pysui/issues/20)

### Changed
- Absolute to relative imports
- Fixed [issue](https://github.com/FrankC01/pysui/issues/12)
- Moved signed transaction handling to sui/sui_rpc.py from faux_wallet
- Moved configuration management to ClientConfig and SuiConfig from faux_wallet
- Moved content of sui/sui_tx_return_types to sui/sui_types
- Fixed typo in transaction return type class `Status`
- Added builder callback for handling RPC response to types (sui/sui_builder.py)
- Changes to support Sui configuration files (both devnet and local) changes for RPC endpoints
- Added new RCP API type introduced 'boolean' in RPC API calls and results
- Simplified requirements.txt
- Added `pysui` to PyPi for ease of installing and using
- Changed sample command line to use `--local` instead of `--cfg`
- When parsing sui configurations, the 'active_env' now drives RPC selection
- Added `build`, and `twine` to `requirements-dev.txt`
- Published 0.0.8 to PyPi
- Published 0.0.9 to PyPi
- Moved `get_type_descriptor` in `faux_wallet.py` heavy lifting to `get_address_object_descriptors` on SuiClient
- Fixed transaction result `deleted` effect for merge-coin transaction to use `GenericRef` result versus `GenericOwnerRef`

### Removed
- sui/sui_tx_return_types.py
- All `events` commands from sample as they've been removed in RPC API in favor of general `sui_getEvents`. Will support in future.
- `get_package_object`
- NFT qualifiers [issue](https://github.com/FrankC01/pysui/issues/21)