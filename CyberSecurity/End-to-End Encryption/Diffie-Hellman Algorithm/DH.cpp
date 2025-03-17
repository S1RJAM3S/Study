// The Diffie-Hellman algorithm is being used to establish a shared secret that can be used for
// secret communications while exchanging data over a public network using the elliptic curve to
// generate points and get the secret key using the parameters.



#include <iostream>
#include <math.h>

using namespace std;



// Implementation: Finite Field Diffie-Hellman
// The parties publicly agree to choose a modulus p and base g
// p: prime
// g: primitive root modulo p
// -> Values are chosen this way to ensure that the resulting shared secret can take on any value from 1 to p-1

long long int FFDH(long long int base,long long int skey, long long int mod) {
    return int(pow(base, skey)) % mod;
}

// TEST
void FFDH_test(long long int p, long long int g, long long int A_skey, long long int B_skey) {
    printf("A secret key is: %d\n", A_skey);
    printf("B secret key is: %d\n", B_skey);
    printf("The publicly chosen modulus and base are: %d and %d\n", p, g);
    long long int A_pkey = FFDH(g, A_skey, p);
    long long int B_pkey = FFDH(g, B_skey, p);
    printf("The key A give to B is: %d\n", A_pkey);
    printf("The key B give to A is: %d\n", B_pkey);
    printf("A mutual key is: %d\n", FFDH(B_pkey, A_skey, p));
    printf("B mutual key is: %d\n", FFDH(A_pkey, B_skey, p));
}

// MAIN
int main() {
    FFDH_test(23, 5, 4, 3);
    return 0;
}