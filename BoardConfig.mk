#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/amazon/tungsten

# Inherit from the common tree
include device/amazon/mt8169-common/BoardConfigCommon.mk

# Inherit the proprietary files
include vendor/amazon/tungsten/BoardConfigVendor.mk
