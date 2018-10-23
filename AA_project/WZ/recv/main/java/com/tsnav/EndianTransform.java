package com.tsnav;

import java.math.BigInteger;

/**
 * User: mac
 * Date: 7/28/15
 * Time: 11:30 PM
 * To change this template use File | Settings | File Templates.
 */

class EndianTransform {
    final private static int mask = 0xFF;
    final private static long longMask = 0xFF;


    public static byte[] serialize(long n) {
        byte[] b = new byte[8];
        int poss = 0;

        for (int i = 0; i < b.length; i++) {
            b[i] = (byte) ((n >> (poss)) & longMask);
            poss += 8;
        }
        return b;
    }


    public static byte[] serialize(int n) {
        byte[] b = new byte[4];
        int poss = 0;

        for (int i = 0; i < b.length; i++) {
            b[i] = (byte) ((n >> poss) & mask);
            poss += 8;
        }
        return b;
    }

    public static int littleToInt(byte[] b) {
        int n = 0;
        int poss = 0;

        for (byte aB : b) {
            n = n | ((aB & mask) << poss);
            poss += 8;
        }
        return n;
    }

    public static int BigToInt(byte[] b) {
        int n = 0;
        int poss = 0;
        byte[] r = reverseArray(b, b.length);
        for (byte aB : r) {
            n = n | ((aB & mask) << poss);
            poss += 8;
        }
        return n;
    }

    public static BigInteger littleToUint64(byte[] b) {
        return new BigInteger(1, b);
    }

    public static BigInteger bigToUint64(byte[] b) {
        return new BigInteger(1, reverseArray(b, b.length));
    }

    private static byte[] reverseArray(byte[] array, int maxLen) {
        byte[] a = new byte[array.length];
        for (int i = 0; i < array.length; i++) {
            a[array.length - i - 1] = array[i];
        }
        if (maxLen != 0) {
            return trimArray(a, maxLen);
        }
        return a;
    }

    private static byte[] trimArray(byte[] array, int size) {
        byte[] a = new byte[size];
        if (array.length > size)
            System.arraycopy(array, 0, a, 0, size);
        else
            System.arraycopy(array, 0, a, 0, array.length);
        return a;
    }
}