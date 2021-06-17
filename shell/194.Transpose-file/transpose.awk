# For each line
{
    # For each field in line
    for (f = 1; f <= NF; f++) {
        # Save field to array
        a[NR, f] = $f
    }
}

# Save maximum number of fields
NF > nf {
    nf = NF
}

# At the end of processing
END {
    # For each field
    for (f = 1; f <= nf; f++) {
        # For each row
        for (r = 1; r <= NR; r++) {
            # Output saved array
            printf a[r, f];

            # Print field or row separator
            printf (r == NR ? RS : FS);
        }
    }
}
