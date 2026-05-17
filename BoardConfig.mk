#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

DEVICE_PATH := device/amazon/tungsten

# Inherit from the common tree
include device/amazon/mt8169-common/BoardConfigCommon.mk

# Display
TARGET_SCREEN_DENSITY := 240

# Kernel Modules
RECOVERY_KERNEL_MODULES += \
    focal_hid.ko \
    i2c-hid-ilitek.ko \
    i2c-hid-nt36523n.ko \
    i2c-hid-of.ko \
    i2c-hid.ko \
    stylus_battery_algo.ko

# Partitions
BOARD_SUPER_PARTITION_SIZE := 4078960640

# Partitions (Dynamic)
BOARD_MAIN_SIZE := 4076863488

# Properties
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop

# Verified Boot
BOARD_AVB_ROLLBACK_INDEX := 2
BOARD_AVB_BOOT_ROLLBACK_INDEX := 7
BOARD_AVB_RECOVERY_ROLLBACK_INDEX := 7

# Inherit the proprietary files
include vendor/amazon/tungsten/BoardConfigVendor.mk
