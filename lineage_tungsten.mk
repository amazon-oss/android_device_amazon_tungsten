#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base.mk)

# Inherit from device makefile.
$(call inherit-product, device/amazon/tungsten/device.mk)

# Inherit some common LineageOS stuff.
$(call inherit-product, vendor/lineage/config/common_full_tablet_wifionly.mk)

PRODUCT_NAME := lineage_tungsten
PRODUCT_DEVICE := tungsten
PRODUCT_MANUFACTURER := Amazon
PRODUCT_BRAND := Amazon
PRODUCT_MODEL := KFTUWI
PRODUCT_CHARACTERISTICS := tablet

PRODUCT_GMS_CLIENTID_BASE := android-amazon

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="tungsten-user 11 RS8338.3339N 0030132734720 amz-p,release-keys" \
    BuildFingerprint=Amazon/tungsten/tungsten:11/RS8338.3339N/0030132734720:user/amz-p,release-keys \
    DeviceProduct=tungsten
